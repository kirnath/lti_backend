from django.urls import path
from . import views

urlpatterns = [
    path('all', views.get_leaves, name='get_leaves'),
    path('create/', views.create_leave, name='create_leave'),
    path('<int:leave_id>/update_state/', views.update_leave_state, name='update_leave_state'),
]
