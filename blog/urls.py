from django.urls import path
from . import views

urlpatterns = [
    # 채울 부분
    path('', views.index),
]