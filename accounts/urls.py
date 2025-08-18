from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/success/', TemplateView.as_view(template_name='accounts/success_page.html'), name='success_page'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),
]