from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import *
from .models import *


def home(request):
    
    return render(request,'app/home.html',)


def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def add_product(request): 
    context={'Product':Product_form()
        
    }
    if request.method == "POST":
        product_form=Product_form(request.POST,request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('/home/product/')
    return render(request,'app/products_add.html',context)

def all_products(request):
    context={'products':Product.objects.all()}
        

    return render(request,'app/products.html',context)
def delete_product(request, id):
    selected_data=Product.objects.get(id=id)
    selected_data.delete() 
    return (redirect('/home/product/'))

def product_update(request, id):
    selected_data = Product.objects.get(id = id)
    context = {
        "Product" : Product_form(instance=selected_data)
        
    }
    if request.method == "POST":
        
        product_form = Product_form(request.POST,request.FILES,instance=selected_data)
        
        if product_form.is_valid():
            
            product_form.save()
            
            return redirect('/home/product/')
        
    return render(request,"app/update.html",context)
    


# views.py

# Create your views here.
