from django import forms
from .models import ExampleModel
import re

class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = ["name", "furigana", "email", "phone_number", "postal_code", "address"]

    # フィールドごとに日本語のラベルを設定
    name = forms.CharField(label="名前*", max_length=50)
    furigana = forms.CharField(label="フリガナ*", max_length=50)
    email = forms.EmailField(label="メールアドレス*")
    phone_number = forms.CharField(label="電話番号*", max_length=15)
    postal_code = forms.CharField(label="郵便番号*", max_length=8)
    address = forms.CharField(label="住所*", widget=forms.Textarea)



    

