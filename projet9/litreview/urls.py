from django.urls import path

from .views import (Flux, CreateTicket, PostUserListView,
                    TicketModifiedUpdateView, Abonnement,
                    ticket_create, CritiqueAnswerCreateview,
                    CritiqueAnswerModified)


urlpatterns = [
    path('', Flux.as_view(), name='litreview-flux'),
    path('createTicket/', CreateTicket.as_view(), name='litreview-createticket'),
    path('createCritique/', ticket_create, name='litreview-createcritique'),
    path('createAnswerCritique/<int:pk>/', CritiqueAnswerCreateview.as_view(), name='litreview-answercritique'),
    path('modifiedAnswerCritique/<int:pk>/', CritiqueAnswerModified.as_view(), name='litreview-modifiedanswercritique'),
    path('posts/', PostUserListView.as_view(), name='litreview-posts'),
    path('modifiedTicket/<int:pk>/', TicketModifiedUpdateView.as_view(), name='litreview-modifiedticket'),
    path('abonnement/', Abonnement.as_view(), name='litreview-Abonnement'),
]