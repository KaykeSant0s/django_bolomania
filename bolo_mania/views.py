from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    return render(request, "home.html", context)

def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    context = {
        "title": "Página de contato",
        "content": "Bem-vindo a página de contato"
    }
    return render(request, "contact/login.html", context) 

def cadastro_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("login")  # ou para onde quiser redirecionar
    else:
        form = UserCreationForm()
    context = {
        "title": "Cadastro",
        "form": form
    }
    return render(request, "contact/view.html", context)
