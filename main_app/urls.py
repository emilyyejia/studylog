from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('problems/', views.problem_index, name='problem_index'),
    path('problems/<int:problem_id>', views.problem_detail, name='problem_detail'),
    path('problems/add', views.ProblemAdd.as_view(), name='problem-add'),
    path('problems/<int:pk>/update/', views.ProblemUpdate.as_view(), name='problem-update'),
    path('problems/<int:pk>/delete/', views.ProblemDelete.as_view(), name='problem-delete'),
    path('problems/<int:problem_id>/add-translation/', views.add_translation, name='add-translation'),
    path('tags/create/', views.TagCreate.as_view(), name='tag-create'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('tags/', views.TagList.as_view(), name='tag-index'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
    
]