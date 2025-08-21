from django.shortcuts import render, redirect, get_object_or_404
from .models import Account # 引入我們剛建立的 Account 模型

def transactions_list(request):
    # middleware 會自動處理 user_profile，因此這裡不需要傳遞 context
    return render(request, 'finance/transactions_list.html')

def categories(request):
    # middleware 會自動處理 user_profile
    return render(request, 'finance/categories.html')

def budgets(request):
    # middleware 會自動處理 user_profile
    return render(request, 'finance/budgets.html')

def accounts_management(request):
    # 處理 POST 請求 (新增、移除、編輯)
    if request.method == 'POST':
        # --- 處理 新增 帳戶 ---
        if 'add_account' in request.POST:
            name = request.POST.get('name')
            account_type = request.POST.get('account_type')
            if name and account_type:
                Account.objects.create(name=name, type=account_type)
        
        # --- 處理 移除 帳戶 ---
        elif 'delete_account' in request.POST:
            account_id = request.POST.get('account_id')
            account = get_object_or_404(Account, pk=account_id)
            account.delete()

        # --- 處理 編輯 帳戶 ---
        elif 'edit_account' in request.POST:
            account_id = request.POST.get('account_id')
            name = request.POST.get('name')
            account_type = request.POST.get('account_type')
            if account_id and name and account_type:
                account = get_object_or_404(Account, pk=account_id)
                account.name = name
                account.type = account_type
                account.save()

        # 處理完畢後，重新導向回本頁面
        return redirect('accounts_management')

    # 處理 GET 請求 (顯示帳戶列表)
    accounts = Account.objects.all() # 從資料庫獲取所有帳戶
    return render(request, 'finance/accounts_management.html', {'accounts': accounts})