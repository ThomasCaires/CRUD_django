from django.shortcuts import render
from .models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy as rl
# Create your views here.
def home(request):
    return render(request, 'users/home.html')

#listar usuario

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'

#criar usuarios
class UserCreateView(CreateView):
    model = User
    fields = ['name', 'age']
    template_name = 'users/user_form.html'
    context_object_name = 'user_form'
    success_url = rl('user_list')
    
#editar usuario
class UserUpdateView(UpdateView):
    model = User
    fields = ['name', 'age']
    template_name = 'users/user_form.html'
    content_type = 'user_update'
    success_url = rl('user_list')

#deletar usuario
class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'