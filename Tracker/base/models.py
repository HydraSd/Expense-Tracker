from http.client import REQUEST_URI_TOO_LONG
from random import choices
from tkinter.tix import Tree
from turtle import mode
from django.db import models
from django.db import models
from matplotlib import image

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    
    def __str__(self):
        return self.user

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    FOOD = 'FD'
    EDUCATION = 'ED'
    TRANSPORT = 'TR'
    ENTERTAINMENT = 'EN'
    HEALTH = 'HE'
    CREDITS = 'CR'
    OTHER = 'OT'

    type_of_choices = [
        (FOOD, 'Food'),
        (EDUCATION, 'Education'),
        (TRANSPORT, 'Transport'),
        (ENTERTAINMENT, 'Entertainment'),
        (HEALTH, 'Health'),
        (CREDITS, 'Credits'),
        (OTHER, 'Other'),
    ]

    Type = models.CharField(max_length=2, choices=type_of_choices, default=FOOD)
    detail = models.TextField(max_length=500, blank=True)
    amount = models.FloatField(null=True, blank=True)
    date = models.DateTimeField("Date of transaction", null=True)
    def __str__(self):
        return self.Type 

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    SALARY = "SL"
    COMMISION= "CO"
    INTEREST = "IN"
    SALES = "SA"
    INVESTMENTS = "IV"
    GIFTS = "GF"
    ALLOWANCE= "AL"

    types_of_incomes = [
        (SALARY, "Salary"),
        (COMMISION, "Commission"),
        (INTEREST, "Interest"),
        (SALES, "Sales"),
        (INVESTMENTS, "Investments"),
        (GIFTS, "Gifts"),
        (ALLOWANCE, "Allowances"),
    ]

    income_ty = models.CharField(max_length=2, choices=types_of_incomes, default=SALARY)
    income_detail = models.TextField(max_length=500, blank=True)
    amount = models.FloatField(null=True, blank=True)
    date = models.DateTimeField("Date of transaction", null=True)
    def __str__(self):
        return self.income_ty

class Classes(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    class_name = models.CharField(max_length=200)
    amount = models.FloatField(null=False)

    def __str__(self):
        return self.class_name

class Payment(models.Model):
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField("Date of Payment", null=True)
    file = models.FileField(null=True, blank=True)
    amount = models.FloatField(null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.description



