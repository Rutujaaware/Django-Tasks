from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('add/', views.menu_create, name='menu_add'),
    path('edit/<int:id>/', views.menu_update, name='menu_edit'),
    path('delete/<int:id>/', views.menu_delete, name='menu_delete'),
]
