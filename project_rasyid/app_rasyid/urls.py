from django.urls import path
from app_rasyid import views

urlpatterns = [
    path('', views.index, name='index'),
]