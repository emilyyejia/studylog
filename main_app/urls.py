from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('problems/', views.problem_index, name='problem_index'),
    path('problems/<int:problem_id>', views.problem_detail, name='problem_detail'),
]