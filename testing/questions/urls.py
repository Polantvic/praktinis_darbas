from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tests/', views.test_list, name='test_list'),
    path('tests/<str:name>/', views.test_questions, name='test_questions'),
    path('tests/<str:name>/<int:pk>/', views.select_answer, name='select_answer'),
]
