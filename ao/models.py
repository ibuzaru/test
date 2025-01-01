# models.py
from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    furigana = models.CharField(max_length=20, null=True, blank=True)
    people = models.CharField(max_length=3, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15,null=True, blank=True)
    postal_code = models.CharField(max_length=8,null=True, blank=True)  # 郵便番号用
    address = models.TextField(null=True, blank=True)  # 住所用

    def __str__(self):
        return self.name


