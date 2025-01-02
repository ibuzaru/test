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
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # フォームが有効な場合はデータを確認画面に渡す
            form_data = form.cleaned_data
            return render(request, 'ao/example_confirm.html', {'data': form_data})

    else:
        check_in = request.GET.get('check_in', '')
        check_out = request.GET.get('check_out', '')
        form = ExampleForm(initial={'check_in_date': check_in, 'check_out_date': check_out})

    return render(request, "ao/example.html", {"form": form})


def example_fix(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)  # 送信されたデータをフォームに渡す
        if form.is_valid():
            # フォームが有効な場合はデータを確認画面に渡す
            form_data = form.cleaned_data
            return render(request, 'ao/example.html', {'data': form_data})
    else:
        form = ExampleForm()  # 初回アクセス時は空のフォーム

    return render(request, "ao/example.html", {"form": form})


def example_confirm(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()  # データを保存
            return redirect('home')  # 保存後にホームへリダイレクト
        else:
            # バリデーションエラー時は再度確認画面を表示
            return render(request, 'ao/example_confirm.html', {'data': request.POST})
    return redirect('example')  # 不正なアクセス時にフォーム入力ページへリダイレクト















