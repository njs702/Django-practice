from django.urls import path
from . import views

urlpatterns = [
    # 채울 부분
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]