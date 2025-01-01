from django import forms
from .models import ExampleModel
import re

class ExampleForm(forms.ModelForm):
    PEOPLE_CHOICES = [(str(i), f"{i}人") for i in range(1, 7)]  # 1～6人の選択肢
    people = forms.ChoiceField(
            choices=PEOPLE_CHOICES,
            label="予約人数",
            widget=forms.Select(attrs={"class": "form-control"})  # 必要に応じてCSSクラスを追加
    )
    class Meta:
        model = ExampleModel
        fields = ["name", "furigana", "people", "email", "phone_number", "postal_code", "address"]

    # フィールドごとに日本語のラベルを設定
    name = forms.CharField(label="名前", max_length=50)
    furigana = forms.CharField(label="フリガナ", max_length=50)
    email = forms.EmailField(label="メールアドレス")
    phone_number = forms.CharField(label="電話番号", max_length=15)
    postal_code = forms.CharField(label="郵便番号", max_length=8)
    address = forms.CharField(label="住所", widget=forms.Textarea)


    

