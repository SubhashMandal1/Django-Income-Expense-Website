from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages

# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    categories=Category.objects.all()
    return render(request, 'expenses/index.html')

def add_expense(request):
    categories=Category.objects.all()
    context={
        'categories':categories,
        'values': request.POST
    }
    if request.method=='GET':
        return render(request, 'expenses/add_expense.html',context)

    if request.method=='POST':
        amount= request.POST['amount']
    
        if not amount:
            messages.error(request, 'Amount is requeired' )
            return render(request, 'expenses/add_expense.html',context)