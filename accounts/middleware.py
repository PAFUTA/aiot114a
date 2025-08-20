# accounts/middleware.py
from .models import UserProfile
from django.utils.deprecation import MiddlewareMixin

class UserProfileMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                request.user.profile = request.user.userprofile
            except UserProfile.DoesNotExist:
                # 為沒有設定檔的使用者建立一個
                request.user.profile = UserProfile.objects.create(user=request.user)