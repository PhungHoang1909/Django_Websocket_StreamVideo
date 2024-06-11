from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_group/', views.create_group, name='create_group'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),
]
