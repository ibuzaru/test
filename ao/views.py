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
            # セッションにデータを保存して確認ページに渡す
            request.session['form_data'] = form.cleaned_data
            return redirect('confirm_example')  # 確認ページにリダイレクト
    else:
        form = ExampleForm()
    return render(request, 'ao/example.html', {'form': form})

def confirm_example(request):
    # セッションからデータを取得
    form_data = request.session.get('form_data', {})
    if not form_data:
        return redirect('example')  # データがない場合、入力ページに戻る
    return render(request, 'ao/confirm_example.html', {'form_data': form_data})

def submit_example(request):
    # セッションからフォームデータを取得
    form_data = request.session.get('form_data')
    if not form_data:
        return redirect('example')  # データがない場合、入力ページに戻る

    # メール送信
    send_mail(
        subject="予約確認",
        message=f"以下の内容で予約を受け付けました:\n\n"
                f"名前: {form_data['name']}\n"
                f"フリガナ: {form_data['furigana']}\n"
                f"メールアドレス: {form_data['email']}\n"
                f"電話番号: {form_data['phone_number']}\n"
                f"住所: {form_data['address']}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[form_data['email']],
    )

    # セッションデータを削除
    request.session.pop('form_data', None)

    # ホーム画面にリダイレクト
    return redirect('home')

