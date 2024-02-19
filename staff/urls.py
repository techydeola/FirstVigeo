from django.urls import path

from . import views

# Define a variable that contains a list of the url patterns
urlpatterns = [
    path('', views.index),
    path('login', views.login_page, name='login'),
    path('logout', views.sign_out, name='logout'),
    path('loan-page/', views.loan_page, name='loan-page'),
    path('loan-page/request', views.loan_request, name='request')
]
