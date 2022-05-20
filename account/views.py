from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Customers, Products, Orders
from .forms import Customers, CustomerForm, OrderForm, ProductForm, UserCreationForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def registerpage(request):
    # form = UserCreationForm()
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = request.POST.get('username')

            messages.success(request, "Successfully account is created for " + user)

            return redirect('login')
    context = {'form': form}
    return render(request, 'crmaccounts/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'username or password is wrong')
    return render(request, 'crmaccounts/login.html')


def home(request):
    customers = Customers.objects.all()
    # products = Products.objects.all()
    orders = Orders.objects.all()
    # orders = Orders.objects.filter(status in ('Delivered','Pending','Outfordelivery'))
    # orders=Orders.objects.filter(status__in=('Delivered','Pending','Outfordelivery'))[0:5]

    total_order = len(orders)
    delivered = orders.filter(status='Delivered', ).count()
    pending = orders.filter(status='Pending').count()
    outfordelivery = orders.filter(status='Outfordelivery').count()

    context = {'customers': customers, 'orders': orders,
               'total_order': total_order,
               'delivered': delivered,
               'pending': pending,
               'outfordelivery': outfordelivery}

    return render(request, 'crmaccounts/dashboard.html', context)


def products(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'crmaccounts/products.html', context)


def customers(request, str_pk):
    customers = Customers.objects.get(id=str_pk)
    orders = customers.orders_set.all()
    total_orders = orders.count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_orders}
    return render(request, 'crmaccounts/customers.html', context)


def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'crmaccounts/order_form.html', context)


def update_order(request, pk):
    order = Orders.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'crmaccounts/order_form.html', context)


def delete_order(request, pk):
    order = Orders.objects.get(id=pk)
    order.delete()
    return redirect('/')


def update_customer(request, pk):
    customer = Customers.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'crmaccounts/update_customer.html', context)


def delete_customer(request, pk):
    customer = Customers.objects.get(id=pk)
    customer.delete()
    return redirect('/')


def update_product(request, pk):
    product = Products.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'crmaccounts/update_product.html', context)


def delete_product(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return redirect('/')


