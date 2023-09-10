from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def home(request):
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img': img, 'form': form})


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/upload.html', {'img': img, 'form': form})

def contact(request):
    return render(request, 'myapp/contact.html')

def cart(request):
    return render(request, 'myapp/cart.html')


def search_prod(request):
    if request.method == "POST":
        searched = request.POST['searched']
        filtered = Image.objects.filter(prod_name__contains = searched)
    form = ImageForm()
    return render(request, 'myapp/home.html', {'img': filtered, 'form': form})
