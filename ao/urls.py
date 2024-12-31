from django.contrib import admin
from django.urls import include, path


from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('resavation/', views.reservation, name="resa"),
   path('contact/', views.contact, name="contact"),
   path('example/', views.example, name='example'),
   path('example_confirm/', views.confirm_example, name='confirm_example'),  # 確認ページ
   path('example_submit/', views.submit_example, name='submit_example'),  # 確定処理
]