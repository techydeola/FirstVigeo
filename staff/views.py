from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RequestForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Loan

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
def loan_page(request):
    user_id = request.user.pk
    loans = Loan.objects.filter(user_id=user_id)
    approved_loan = loans.filter(status=2) #querying for all approved loans
    total_app = 0
    for loan in approved_loan:
        total_app += loan.loan_amount
    return render(request, 'staff/loan-page.html', {"loans": loans, "total_app": total_app})

@login_required(login_url='login')
def sign_out(request):
    logout(request)
    del request.session
    messages.success(request, f'You have been logged out')
    return redirect(reverse('login'))


@login_required(login_url='login')
def loan_request(request):
    if request.method == 'GET':
        form = RequestForm()
        return render(request, 'staff/loan_request.html', {'request_form': form})
    
    if request.method == 'POST':
        user_instance = request.user
        loan_amount = request.POST['loan_amount']
        Loan.objects.create(user_id=user_instance, loan_amount=loan_amount)
        messages.success(request, f'Your Loan has been submitted')
        return redirect(reverse('loan-page') + '?request_submitted=True')



def index(request):
    return render(request, 'staff/index.html')