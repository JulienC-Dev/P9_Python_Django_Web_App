from django.urls import path
from .views import MyLoginView, SignUpView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', MyLoginView.as_view(template_name='authentication/loginhome.html'), name='login-user'),
    path('inscription/', SignUpView.as_view(), name='form-inscription'),
    path('logout/', LogoutView.as_view(template_name='authentication/logout.html'), name='logout-user'),
]