from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Review, Ticket
from authentication.models import User
from litreview.forms import CreateTicket, ModifiedTicket, CreateCritique
from django.views.generic import CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.contrib.contenttypes.models import ContentType


class FluxView(LoginRequiredMixin, ListView):
    template_name = 'litreview/flux.html'

    def get_queryset(self):
        user_following_by = self.request.user.following_by.values('user')
        review_following = Review.objects.filter(user__in=user_following_by)
        review_answer = Review.objects.exclude(user=self.request.user).filter(ticket__user=self.request.user)
        user_review = Review.objects.filter(user=self.request.user)
        qs_review = user_review.union(review_following)
        ticket_following = Ticket.objects.filter(user__in=user_following_by)
        user_ticket = Ticket.objects.filter(user=self.request.user)
        qs_ticket = user_ticket.union(ticket_following)
        posts = sorted(chain(qs_review, qs_ticket, review_answer), key=lambda post: post.time_created, reverse=True)
        qs = [{ContentType.objects.get_for_model(type(x)).name: x} for x in posts]
        return qs


class CreateTicketView(LoginRequiredMixin, CreateView):
    template_name = 'litreview/createticket.html'
    form_class = CreateTicket
    success_url = reverse_lazy('litreview-flux')
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class CritiqueAnswerCreateview(LoginRequiredMixin, CreateView):
    template_name = "litreview/critiqueanswercreate.html"
    success_url = reverse_lazy('litreview-flux')
    form_class = CreateCritique

    def get_context_data(self, **kwargs):
        object = super(CritiqueAnswerCreateview, self).get_context_data(**kwargs)
        object['ticket'] = self.get_object()
        return object

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Ticket.objects.get(pk=pk)

    def form_valid(self, form):
        ticket_obj = self.get_object()
        form.instance.ticket = ticket_obj
        form.instance.user = self.request.user
        ticket_obj.answer_review = True
        ticket_obj.save()
        form.instance.answer_review = True
        return super().form_valid(form)


class CritiqueAnswerModified(LoginRequiredMixin, UpdateView):
    template_name = 'litreview/critiqueanswermodified.html'
    form_class = CreateCritique
    model = Review
    success_url = reverse_lazy('litreview-posts')

    def get_context_data(self, **kwargs):
        context = super(CritiqueAnswerModified, self).get_context_data(**kwargs)
        context['ticket'] = self.object.ticket
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Review.objects.get(pk=pk)


class PostUserListView(LoginRequiredMixin, ListView):
    template_name = 'litreview/postuser.html'
    success_url = reverse_lazy('litreview-posts')

    def get_queryset(self):
        user_review = Review.objects.filter(user=self.request.user)
        user_ticket = Ticket.objects.filter(user=self.request.user)

        posts = sorted(chain(user_review, user_ticket), key=lambda post: post.time_created, reverse=True)
        qs = [{ContentType.objects.get_for_model(type(x)).name: x} for x in posts]
        return qs

    def post(self, request):
        try:
            ticket_obj = self.request.POST.get('delete-ticket')
            review_obj = self.request.POST.get('delete-review')
            if ticket_obj is not None:
                Ticket.objects.get(id=ticket_obj).delete()
            if review_obj is not None:
                Review.objects.get(id=review_obj).delete()
        except:
            return redirect(self.success_url)
        return redirect(self.success_url)


class TicketModifiedUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'litreview/modifiedticket.html'
    form_class = ModifiedTicket
    model = Ticket
    success_url = reverse_lazy('litreview-posts')


class AbonnementView(LoginRequiredMixin, View):
    template_name = 'litreview/abonnement.html'

    def get(self, request):
        dict_query = self.request.GET
        query = dict_query.get('q')
        user_object = None

        if query is not None:
            try:
                user_object = User.objects.get(username=query)
            except:
                message = 'l utilisateur n existe pas'
                return render(request, self.template_name, {'message': message,
                       'userfollows': self.request.user.following_by.all(),
                       'userflollowings': self.request.user.following.all()})

        context = {'object': user_object,
                   'userfollows': self.request.user.following_by.all(),
                   'userflollowings': self.request.user.following.all()}
        return render(request, self.template_name, context)

    def post(self, request):
        dict_query = self.request.POST
        query = dict_query.get('follow')
        if query is not None:
            user = User.objects.get(username=query)
            try:
                target_user = user.following.get(user=user)
                if target_user is not None:
                    context = {'userfollows': self.request.user.following_by.all(),
                               'userflollowings': self.request.user.following.all(),
                               'message': 'Vous êtes déjà abonné'
                               }
                    return render(request, self.template_name, context)
            except:
                user.following.create(followed_user=self.request.user)
                context = {'userfollows': self.request.user.following_by.all(),
                           'userflollowings': self.request.user.following.all()}
                return render(request, self.template_name, context)

        else:
            query = dict_query.get('unfollow')
            user = User.objects.get(username=query)
            self.request.user.following_by.filter(user=user).delete()
            context = {'userfollows': self.request.user.following_by.all(),
                       'userflollowings': self.request.user.following.all()}
            return render(request, self.template_name, context)


@login_required()
def ticket_create(request):
    if request.method == 'POST':
        ticket_form = CreateTicket(request.POST)
        critique_form = CreateCritique(request.POST)
        if ticket_form.is_valid() and critique_form.is_valid():
            ticket_form.instance.user = request.user
            ticket_form.instance.answer_review = True
            ticket = ticket_form.save()
            critique_form.instance.ticket = ticket
            critique_form.instance.answer_review = True
            critique_form.instance.user = request.user
            critique_form.save()
            return redirect('litreview-flux')
    else:
        ticket_form = CreateTicket()
        critique_form = CreateCritique()
    return render(request, 'litreview/createcritique.html', {'ticket_form': ticket_form, 'critique_form': critique_form})

