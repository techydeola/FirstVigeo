from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RequestForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Loan

# Create your views here.

# create the login page view
def login_page(request):
    if request.method == 'GET':
        # check if user is authenticated and redirects to the user loan page
        if request.user.is_authenticated:
            return HttpResponseRedirect('loan-page')
        
        # otherwise, create an instance of the login form and pass to the login template
        form = LoginForm()
        return render(request, 'staff/login.html', {'form': form})
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # checks if form is valid
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # authenticates using the username and password from the form
            user = authenticate(request=request, username=username, password=password)

            # logs the user in if user exist
            if user:
                login(request, user)
                return HttpResponseRedirect('loan-page')

        # renders the login template with error if form is not valid
        # or user login details does not match     
        messages.error(request, f'Invalid username or password')
        return render(request, 'staff/login.html', {'form': form})


@login_required(login_url='login')
# create the loan page view
def loan_page(request):
    user_id = request.user.pk
    loans = Loan.objects.filter(user_id=user_id)
    approved_loan = loans.filter(status=2) # querying for all approved loans
    total_app = 0
    for loan in approved_loan:
        total_app += loan.loan_amount
    return render(request, 'staff/loan-page.html', {"loans": loans, "total_app": total_app})

@login_required(login_url='login')
# create the sign out view
def sign_out(request):
    logout(request)
    # delete the user session
    del request.session
    messages.success(request, f'You have been logged out')
    return redirect(reverse('login'))


@login_required(login_url='login')
# create the loan request view
def loan_request(request):
    if request.method == 'GET':
        # create an instance of the loan request form
        form = RequestForm()
        return render(request, 'staff/loan_request.html', {'request_form': form})
    
    if request.method == 'POST':
        user_instance = request.user
        loan_amount = request.POST['loan_amount']
        # create a loan instance and save to the database
        Loan.objects.create(user_id=user_instance, loan_amount=loan_amount)
        messages.success(request, f'Your Loan has been submitted')
        return redirect(reverse('loan-page') + '?request_submitted=True')



# create the landing page view
def index(request):
    return render(request, 'staff/index.html')