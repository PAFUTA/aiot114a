from django.shortcuts import render

def transactions_list(request):
    return render(request, 'finance/transactions_list.html')

def categories(request):
    return render(request, 'finance/categories.html')

def budgets(request):
    return render(request, 'finance/budgets.html')

def settings(request):
    return render(request, 'finance/settings.html')