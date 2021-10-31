import json
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

import random
import csv



from functools import wraps
from urllib.parse import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.shortcuts import reverse, redirect
from django.utils.http import urlencode
from django import forms




#from .forms import  CustomUserCreationForm 
#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.views.generic.edit import CreateView, UpdateView, DeleteVie


# Create your views here ---------------------------------------------------

from .models import Post , Categoria
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages 


#----------------------------------------------------------------------------

def registro(request):
    data= {'form': CustomUserCreationForm()}

    if request.method =="POST":
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],
            password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado OK.")
            return redirect('/')
        data["form"] = formulario      
    return render(request, 'registration/registro.html', data)



def index(request):
    queryset = request.GET.get('buscar')
    ###########################################################
    # Consulta en Postgrest                                   #
    # SELECT * from app_blog_4_post WHERE estado = 't';       #
    ###########################################################
    posts = Post.objects.filter(estado=True)
    ###########################################################
    # SELECT * FROM app_blog_4_post                           #
    # WHERE                                                   #
    # description LIKE '%prueba%'                              #
    # or                                                      #
    # titulo like '%prueba%';                                  #
    ###########################################################
    if queryset :
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,2) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}

    return render(request,'app_blog/index.html', context)


def generales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact='General')
    )
    if queryset :
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria = Categoria.objects.get(nombre__iexact='General'),
        ).distinct()
    
    paginator = Paginator(posts,2) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    context = {'posts': posts}
    return render(request,'app_blog/generales.html', context)


def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact='Programación')
    )
    if queryset :
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria = Categoria.objects.get(nombre__iexact='Programación'),
        ).distinct()
    
    paginator = Paginator(posts,2) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    context = {'posts': posts}
    return render(request,'app_blog/programacion.html', context)


def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact='Video Juegos')
    )
    if queryset :
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria = Categoria.objects.get(nombre__iexact='Video Juegos'),
        ).distinct()
    
    paginator = Paginator(posts,2) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    context = {'posts': posts}
    return render(request,'app_blog/videojuegos.html', context)



def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact='Tecnología')
    )
    if queryset :
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria = Categoria.objects.get(nombre__iexact='Tecnología'),
        ).distinct()
    
    paginator = Paginator(posts,2) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    context = {'posts': posts}
    return render(request,'app_blog/tecnologia.html', context)



def tutoriales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact='Tutoriales')
    )
    if queryset :
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria = Categoria.objects.get(nombre__iexact='Tutoriales'),
        ).distinct()
    
    paginator = Paginator(posts,2) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    context = {'posts': posts}
    return render(request,'app_blog/tutoriales.html', context)


def post(request,slug):
    post =get_object_or_404(Post, slug=slug)
    context ={'post':post}
    return render(request,'app_blog/post.html',context)


