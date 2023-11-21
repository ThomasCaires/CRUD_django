from django.urls import path
from app_CRUD import views

urlpatterns = [
    #route, view, reference
    #pagina inicial
    path('',views.home,name='home'),
    path('users/',views.users,name='user_list')
]
