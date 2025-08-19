from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        # 如果使用者提交表單
        form = SignupForm(request.POST)
        if form.is_valid():
            # 如果表單驗證成功
            form.save()
            return redirect('success_page') # 稍後會建立這個頁面
    else:
        # 如果是 GET 請求，顯示空的表單
        form = SignupForm()
    
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)