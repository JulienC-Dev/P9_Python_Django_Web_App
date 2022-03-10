from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import signup_page
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login


class myAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Votre nom ou mots de passe ne correspondent pas. Merci de réessayer."
        ),
        'inactive': ("Ce compte est inactif."),
    }


class MyLoginView(LoginView):
    authentication_form = myAuthForm


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'authentication/inscription.html'
    form_class = signup_page
    success_message = "Votre profile est correctement créé"
    success_url = reverse_lazy('litreview-flux')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid




