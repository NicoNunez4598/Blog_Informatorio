from django.shortcuts import render, redirect
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from .models import Autor, Categoria
from .forms import CustomUserCreationForm

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

def exit(request):
    logout(request)
    return redirect('inicio')

def autores(request):
    autoreslistados = Autor.objects.all()
    return render(request, 'autores.html', {"autoreslistados" : autoreslistados})

def registrarautor(request):

    nombres=request.POST['txtNombres']
    apellidos=request.POST['txtApellidos']
    facebook=request.POST['txtFacebook']
    twitter=request.POST['txtTwitter']
    instagram=request.POST['txtInstagram']
    web=request.POST['txtWeb']
    correo=request.POST['email']
    estado=True

    autor= Autor.objects.create(nombres=nombres, apellidos=apellidos, facebook=facebook, twitter=twitter, instagram=instagram, web=web, correo=correo, estado=estado)

    messages.success(request, 'Se ha registrado un autor')

    return redirect('autores')

def edicionautor(request, id):

    autor = Autor.objects.get(id=id)

    return render(request, 'edicionAutores.html', {"autor":autor})

def editarautor(request):

    id = request.POST['numberid']
    nombres=request.POST['txtNombres']
    apellidos=request.POST['txtApellidos']
    facebook=request.POST['txtFacebook']
    twitter=request.POST['txtTwitter']
    instagram=request.POST['txtInstagram']
    web=request.POST['txtWeb']
    correo=request.POST['email']
    estado=request.POST['estado']

    autor = Autor.objects.get(id=id)
    autor.nombres = nombres
    autor.apellidos = apellidos
    autor.facebook = facebook
    autor.twitter = twitter
    autor.instagram = instagram
    autor.web = web
    autor.correo = correo
    autor.estado = estado

    autor.save()

    messages.success(request, 'Se ha editado con exito el autor seleccionado')

    return redirect('autores')

def eliminarautor(request, id):
    
    autor = Autor.objects.get(id=id)

    autor.delete()

    messages.success(request, 'Se ha eliminado el autor seleccionado')

    return redirect('autores')

def categorias(request):
    categoriaslistadas = Categoria.objects.all()
    return render(request, 'categorias.html', {"categoriaslistadas" : categoriaslistadas})

def registrarcategoria(request):

    nombre=request.POST['txtNombre']
    estado=True

    categoria = Categoria.objects.create(nombre=nombre, estado=estado)

    messages.success(request, 'Se ha registrado una categoria')

    return redirect('categorias')

def edicioncategoria(request, id):

    categoria = Categoria.objects.get(id=id)

    return render(request, 'edicionCategorias.html', {"categoria":categoria})

def editarcategoria(request):

    id = request.POST['numberid']
    nombre=request.POST['txtNombre']
    estado=request.POST['estado']

    categoria = Categoria.objects.get(id=id)
    categoria.nombre = nombre
    categoria.estado = estado

    categoria.save()

    messages.success(request, 'Se ha editado con exito la categoria seleccionada')

    return redirect('categorias')

def eliminarcategoria(request, id):
    
    categoria = Categoria.objects.get(id=id)

    categoria.delete()

    messages.success(request, 'Se ha eliminado la categoria seleccionada')

    return redirect('categorias')

def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    return render(request, 'registration/register.html', data)