from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('updatetask/<str:pk>/', views.updatetask, name='updatetask'),
    path('changestatus/<str:pk>/', views.changestatus, name='changestatus'),
    path('deletetask/<str:pk>/', views.deletetask, name='deletetask'),
    path('addtask/', views.addtask, name='addtask'),
]
