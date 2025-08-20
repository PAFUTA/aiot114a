# finance/views.py
from django.shortcuts import render

def transactions_list(request):
    # middleware 會自動處理 user_profile，因此這裡不需要傳遞 context
    return render(request, 'finance/transactions_list.html')

def categories(request):
    # middleware 會自動處理 user_profile
    return render(request, 'finance/categories.html')

def budgets(request):
    # middleware 會自動處理 user_profile
    return render(request, 'finance/budgets.html')