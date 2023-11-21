from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def users(request):
    #salvar os dadosda tela no Database
    new_user = User()
    new_user.name = request.POST.get("name")
    new_user.age = request.POST.get("age")
    new_user.save()
    #exibir os users cadastrados na pagina
    users = {
        'users' : User.objects.all()
    }
    #retornar dados para a pagina de listagem
    return render(request, 'users/users.html', users)