from django.urls import path, include
from app_CRUD.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView
from django.contrib import admin

urlpatterns = [
    #route, view, reference
    path('',UserListView.as_view(),name='user_list'),
    path('users',UserCreateView.as_view(),name='users_create'),
    path('users/<int:pk>/',UserUpdateView.as_view(),name='user_update'),
    path('users/<int:pk>/',UserDeleteView.as_view(),name='user_delete'),
    #admin
    path('admin/', admin.site.urls),  
]
