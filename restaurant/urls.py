from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(), name='menuitem-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(),
         name='menuitem-detail'),
]
