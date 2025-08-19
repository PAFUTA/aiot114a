from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    # 這個類別繼承了 Django 內建的使用者創建表單
    # 這讓我們可以輕鬆地創建帳號、密碼等欄位
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')