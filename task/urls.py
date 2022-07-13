from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('updatetask/<int:id>', views.updatetask, name='updatetask'),
    path('<int:id>/', views.view_tasks, name='view_tasks'),
]
