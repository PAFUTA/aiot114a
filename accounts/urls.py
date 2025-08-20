# accounts/urls.py

from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 處理使用者註冊頁面的路徑
    path('signup/', views.signup, name='signup'),
    
    # 註冊成功後導向頁面的路徑
    path('signup/success/', TemplateView.as_view(template_name='accounts/success_page.html'), name='success_page'),
    
    # 使用者登出功能的處理路徑
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),
    
    # 新增的設定頁面路徑
    path('settings/', views.settings, name='settings'),
]