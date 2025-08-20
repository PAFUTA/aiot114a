# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 在使用者註冊成功後，立即為他們建立 UserProfile
            UserProfile.objects.create(user=user)
            messages.success(request, '恭喜！註冊成功，請登入。')
            return render(request, 'accounts/success_page.html')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def settings(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        theme = request.POST.get('theme')
        font_size = request.POST.get('font_size')

        # 這兩行是關鍵的除錯語句
        print("--- 開始除錯 ---")
        print(f"收到的主題：{theme}")
        print(f"收到的字體大小：{font_size}")
        print("--- 結束除錯 ---")

        user_profile.theme = theme
        user_profile.font_size = font_size
        user_profile.save()
        messages.success(request, '設定已成功儲存！')
        return redirect('settings')

    context = {
        'user_profile': user_profile
    }
    return render(request, 'accounts/settings.html', context)