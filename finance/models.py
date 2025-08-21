# finance/models.py

from django.db import models

class Account(models.Model):
    # 帳戶名稱 (例如：國泰世華活存)
    name = models.CharField(max_length=100)
    
    # 帳戶類型 (銀行或證券)
    ACCOUNT_TYPES = [
        ('bank', '銀行帳戶'),
        ('securities', '證券帳戶'),
    ]
    type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    
    # 其他你可能需要的欄位
    # balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"