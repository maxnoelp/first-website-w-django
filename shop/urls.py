from django.urls import path
from . import views

urlpatterns=[
    path('', views.shop, name='shop'),
    path('warenkorb/', views.card, name='card'),
    path('kasse/', views.checkout, name='checkout')
]