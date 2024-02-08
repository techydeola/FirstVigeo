from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RequestForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Loan, Staff

# Create your views here.

def login_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect('loan-page')
        
        form = LoginForm()
        return render(request, 'staff/login.html', {'form': form})
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect('loan-page')
            
        messages.error(request, f'Invalid username or password')
        return render(request, 'staff/login.html', {'form': form})


@login_required(login_url='login')
def index(request):
    return render(request, 'staff/loan-page.html')

@login_required(login_url='login')
def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out')
    return HttpResponseRedirect('login')


@login_required
def loan_request(request):
    if request.method == 'GET':
        form = RequestForm()
        return render(request, 'staff/loan_request.html', {'request_form': form})
    
    if request.method == 'POST':
        user_instance = request.user
        # user = Staff.objects.get(pk=user_id)
        loan_amount = request.POST['loan_amount']
        loan_instance = Loan.objects.create(user_id=user_instance, loan_amount=loan_amount)
        messages.success(request, f'Your Loan has been submitted')
        return HttpResponseRedirect('loan-page')