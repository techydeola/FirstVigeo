from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Staff(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, validators=[MaxLengthValidator(11), MinLengthValidator(11)], null=True)
    account_name = models.CharField(null=False, max_length=100)
    account_number = models.CharField(validators=[MaxLengthValidator(10), MinLengthValidator(10)
    ], max_length=100)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staffs"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Status(models.Model):
    LOAN_STATUS_CHOICES = (
        ('rejected', 'Rejected'),
        ('approved', 'Approved'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=20, null=True, choices=LOAN_STATUS_CHOICES)

    def __str__(self):
        return self.status

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    loan_amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, default=3)
    managers_comment = models.TextField(blank=True)

    def __str__(self):
        return str(self.loan_amount)


class LoanDetail(models.Model):
    amount_paid = models.ForeignKey(Loan, on_delete=models.CASCADE)
