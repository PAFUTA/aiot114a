from django.db import models
from django.contrib.auth.models import User # 引入 Django 內建的使用者模型

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', '收入'),
        ('expense', '支出'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.date} - {self.description} ({self.amount})"