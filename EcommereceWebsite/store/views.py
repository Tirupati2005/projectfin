from django.shortcuts import render,redirect
import requests
import json
from .forms import ProductForm,OrderForm
from .models import Product,Category,ProductImage
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Order,Customer
#from store.middlewares.auth import auth_middleware



def home(request):
    try:
    
        url = 'https://dummyjson.com/products'
        response = requests.get(url)
        response.raise_for_status()  

        products_data = response.json().get('products', [])

        for product_data in products_data:
               
                category_name = product_data['category']
                category_instance, _ = Category.objects.get_or_create(name=category_name)


                product_instance = Product(
                    name=product_data['title'],
                    price=product_data['price'],
                    category=category_instance,
                    description=product_data['description'],
                    title=product_data['title'],

                    
                )

                product_instance.save()
        return render(request, 'store/upload.html', {'products_data': products_data})

    
    except requests.RequestException as e:
        
        error_message = f"Failed to fetch data from API: {e}"
        return render(request, 'store/upload.html', {'error_message': error_message})




def login_user(request): 
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,("You have been logged in...!"))
                return redirect('home')
            else:
                messages.success(request,("There was an Error,Please try again...!"))
                return redirect('login')
        else:
            return render(request, 'store/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')


def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("You have been Signup successfully...Welcome!"))
            return redirect('home')
        else:
            messages.success(request,("There was a problem in Resistering...Try again!"))
            return redirect('signup')

    else:    
        return render(request,'store/signup.html', {'form':form})





def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_user=form.save()
            messages.success(request,("Product Added successfully...!"))
            return redirect('home')
        else:
            messages.success(request,("Product Added successfully...!"))
            return redirect('add')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})









def edit_product(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,("Edited Product successfully...!"))
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/edit_product.html', {'form': form})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request,("Deleted Product successfully...!"))
        return redirect('product_list')
    return render(request, 'store/delete_product.html', {'product': product})









@login_required
def order_product(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("Product Ordered successfully...!"))
            return redirect('home')
        else:
            messages.success(request,("Product are not find try again...!"))
            return redirect('order')
    else:
        form = OrderForm()
    return render(request, 'store/order.html', {'form': form})


def basepage(request):
    return render(request,'store/base.html')






