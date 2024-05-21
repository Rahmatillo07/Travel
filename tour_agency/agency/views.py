from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .models import Ticket, Company, Category
from .forms import TicketForm, CategoryForm, CompanyForm, LoginForm, RegisterForm


def all_tickets(request):
    tickets = Ticket.objects.all()
    companies = Company.objects.all()
    categories = Category.objects.all()

    context = {
        'tickets': tickets,
        'companies': companies,
        'categories': categories
    }
    return render(request, 'agency/index.html', context)


def category_by_ticket(request, category_id):
    tickets = Ticket.objects.filter(category_id=category_id)
    company = Company.objects.all()
    categories = Category.objects.all()

    context = {
        'tickets': tickets,
        'companies': company,
        'categories': categories
    }
    return render(request, 'agency/index.html', context)


def detail(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    categories = Category.objects.all()

    context = {
        'ticket': ticket,
        'categories': categories
    }
    return render(request, 'agency/detail.html', context)



def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TicketForm()

    context = {
        'form': form
    }
    return render(request, 'agency/create.html', context=context)



def update_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    form = TicketForm(data=request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('phone_detail',pk=pk)
    context = {
        'form': form
    }
    return render(request,'agency/create.html',context=context)


def delete_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('index')

    context = {
        'ticket': ticket
    }
    return render(request,'agency/delete.html',context)





def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f'{user.username} saytga muvaffaqiyatli kirdingiz!')
        return redirect('index')
    return render(request, 'agency/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def user_register(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f"{user.username} royxatdan muvaffaqiyatli o'tdingiz")
        return redirect('login')
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'agency/register.html', context)

# Create your views here.
