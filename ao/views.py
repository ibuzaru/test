from django.shortcuts import render, redirect
from .forms import ExampleForm

from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'ao/home.html')

def reservation(request):
    return render(request, 'ao/reservation.html')

def contact(request):
    return render(request, 'ao/contact.html')

def test(request):
    return render(request, 'ao/test.html')



def example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # フォームデータをセッションに保存
            request.session['form_data'] = form.cleaned_data

                    # チェックイン日とチェックアウト日を取得
        check_in_date = request.POST.get("check_in_date")
        check_out_date = request.POST.get("check_out_date")

        # 予約データをテンプレートに渡す
        return render(request, 'ao/example.html', {
            'check_in_date': check_in_date,
            'check_out_date': check_out_date,
            'form': form,  # フォームもテンプレートに渡す
        })
    else:
        # セッションからフォームデータを取得
        form_data = request.session.get('form_data', None)
        if form_data:
            form = ExampleForm(initial=form_data)
        else:
            form = ExampleForm()

    return render(request, 'ao/example.html', {'form': form})








