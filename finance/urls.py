from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transactions_list, name='transactions_list'), # 記帳
    path('categories/', views.categories, name='categories'), # 類別管理
    path('budgets/', views.budgets, name='budgets'), # 預算設定
]