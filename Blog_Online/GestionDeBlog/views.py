from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'index.html', {'post':post})

def generales(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Generales'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Generales')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'generales.html', {'post':post})

def programacion(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Programacion'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'programacion.html', {'post':post})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'videojuegos.html', {'post':post})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'tecnologia.html', {'post':post})

def tutoriales(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
        ).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'tutoriales.html', {'post':post})

def detallepost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detallepost':post})