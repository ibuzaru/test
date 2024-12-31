from django.shortcuts import render, redirect
from .forms import ExampleForm

def example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # セッションにデータを保存して確認ページに渡す
            request.session['form_data'] = form.cleaned_data
            return redirect('confirm_example')  # 確認ページにリダイレクト
    else:
        form = ExampleForm()
    return render(request, 'example.html', {'form': form})

def confirm_example(request):
    # セッションからデータを取得
    form_data = request.session.get('form_data', {})
    if not form_data:
        return redirect('example')  # データがない場合、入力ページに戻る
    return render(request, 'confirm_example.html', {'form_data': form_data})



