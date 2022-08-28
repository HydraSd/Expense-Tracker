
from re import template
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from matplotlib.style import context
from requests import request
from .models import *
from .forms import *
from .filters import *
from collections import OrderedDict
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login')    

    context = {
        "form":form,
    }
    return render(request, 'base/register.html', context)

def login_page(request):
    context = {

    }
    return render(request, 'base/login.html', context)

def home(request):
    users = User.objects.order_by('-user')
    expenses_amount = Expense.objects.all()

    if len(expenses_amount) > 0:
        expenses_total = sum([total.amount for total in expenses_amount])
        #expenses_max = max([total.Type for total in expenses_amount])
        expenses_max_amount = max([total.amount for total in expenses_amount])
    else:
        expenses_total = 0
        expenses_max_amount = 0
    print(len(expenses_amount))
   

# incomes
    income_amount = Income.objects.all()
    if len(income_amount) > 0:
        income_total = sum([total.amount for total in income_amount])
    else:
        income_total = 0

#Classes
    Classes_t = Payment.objects.all()
    if len(Classes_t) > 0:
        total_fees = sum([total.amount for total in Classes_t])
    else:
        total_fees = 0

# Details
    expenses = Expense.objects.order_by('-Type')
    incomes = Income.objects.order_by('-income_ty')


    context = {
        "users" : users,
        'expenses_total': expenses_total,
        "expenses_max_amount" : expenses_max_amount,
        "income_total" : income_total,
        "expenses" : expenses,
        "incomes" : incomes,
        "total_fees":total_fees,
    }
    return render(request, 'base/home.html', context)
       
def expenses_data(request):
    global values
    users = User.objects.order_by('-user')
    expenses = Expense.objects.all()
    incomes = Income.objects.order_by('-income_ty')

    expense_filter = ExpenseFilter(request.GET, queryset=expenses)
    expenses = expense_filter.qs
    if len(expenses) > 0 :
        total = sum([total.amount for total in expenses])
        values = [item.amount for item in expenses]
        max_val = max([total.amount for total in expenses])
        min_val = min([total.amount for total in expenses])
        ty = [i.Type for i in expenses]
        # food = 0
        # education = 0 
        # transport = 0
        # entertainment = 0
        # health = 0
        # credits = 0 
        for i in values:
            print(values)
    else:
        total = 0
        values = []
   
    content = {
        "total" : total,
        "expenses" : expenses,
        "incomes" : incomes,
        "users" : users,
        "expense_filter":expense_filter,
        "values" : values,
        "max":max_val,
        "min":min_val
        
    }
    return render(request, 'base/expense_data.html', content)

# def expense_form(request):
#     context = {}
#     return render(request, 'base/expense_form.html', context)

# Classes
def classes(request):
    user = Classes.objects.order_by('-name')
    class_name = Classes.objects.order_by('-class_name')
    amount = Classes.objects.order_by('-amount')
    form = ClassForm()
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "class_name" : class_name,
        "amount": amount,
        "form":form
    }
    return render(request, 'base/classes.html', context)

def new_class(request):
    form = ClassForm()
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        "form":form,
    }
    return render(request, 'base/classes_form.html', context)

def update_class(request, pk):
    class_name = Classes.objects.get(id=pk)
    form = ClassForm(instance=class_name)
    if request.method == "POST":
            form = ClassForm(request.POST, instance=class_name)
            if form.is_valid():
                form.save()
                return redirect('/')
    context = {"form":form}
    return render(request, 'base/classes_form.html', context)

def delete_class(request,pk):
    class_name = Classes.objects.get(id=pk)
    if request.method == "POST":
        class_name.delete()
        return redirect('/')
    context = {"item":class_name}
    return render(request, 'base/classes_delete.html', context)

#Payments
def payment(request):
    payments = Payment.objects.all()
    payment_filter = PaymentFilter(request.GET, queryset=payments)
    payments = payment_filter.qs
    if len(payments) > 0:
        total_fees = sum([total.amount for total in payments])
        class1 = [item.class_name for item in payments]
        amount = [item.amount for item in payments]
        max_val = max([total.amount for total in payments])
        min_val = min([total.amount for total in payments])
        print(amount)
    else:
        total_fees = 0
        class1 = []
        amount = []
        max_val = 0
        min_val = 0
    context = {
        'payments':payments,
        "total_fees":total_fees,
        "payment_filter":payment_filter,
        "class":class1,
        "amount":amount,
        "max":max_val,
        "min":min_val
    }
    return render(request, './base/payments.html', context)
# Payment Form
def new_payment(request):
    form = PaymentsForm()
    if request.method == "POST":
        form = PaymentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'base/payment_form.html', context)

def payment_update(request,pk):
    description = Payment.objects.get(id=pk)
    form = PaymentsForm(instance = description)
    if request.method == "POST":
        form = PaymentsForm(request.POST, request.FILES, instance=description)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'base/payment_form.html', context)

def payment_delete(request,pk):
    description = Payment.objects.get(id=pk)
    if request.method == "POST":
        description.delete()
        return redirect('/')
    context = {'item':description}
    return render(request, 'base/payment_delete.html', context)

def new_expense(request):
    form = ExpenseForm()
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    
    
    context = {
        "form":form,
    }
    return render(request, 'base/expense_form.html', context)

def update_expense(request,pk):
    type = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=type)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={"form":form}
    return render(request, 'base/expense_form.html', context)

def expense_delete(request,pk):
    type = Expense.objects.get(id=pk)
    if request.method == "POST":
        type.delete()
        return redirect('/')
    context = {'item':type}
    return render(request, 'base/expense_delete.html', context)

def income_detail(request):
    incomes = Income.objects.all()
    income_filter = IncomeFilter(request.GET, queryset=incomes)
    incomes = income_filter.qs
    if len(incomes) > 0:
        total = sum([total.amount for total in incomes])
        max_paid = max([item.amount for item in incomes])
        min_paid = min([item.amount for item in incomes])
        print(max_paid)
    else:
        total = 0
        max_paid = 0
        min_paid = 0
    context = {
        "total":total,
        "incomes":incomes,
        "income_filter":income_filter,
        "max":max_paid,
        "min":min_paid,
        }
    return render(request, 'base/income.html', context)

def new_income(request):
    form = IncomeForm()
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form":form}
    return render(request, 'base/income_form.html', context)

def update_income(request,pk):
    income_ty = Income.objects.get(id=pk)
    form = IncomeForm(instance=income_ty)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income_ty)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form":form}
    return render(request, 'base/income_form.html', context)

def income_delete(request, pk):
    income_ty = Income.objects.get(id=pk)
    if request.method == "POST":
        income_ty.delete()
        return redirect('/')
    context = {"income":income_ty}
    return render(request, 'base/income_delete.html', context)


def items(request):
    return render(request, 'base/buy.html')




def render_pdf_main(template_src, context={}):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

exp = Expense.objects.all()
inc = Income.objects.all()
pay = Payment.objects.all()



if len(exp) > 0 and len(inc) > 0 and len(pay) > 0:
    total_exp = sum([total.amount for total in exp])
    total_inc = sum([total.amount for total in inc])
    total_pay = sum([total.amount for total in pay])
    exp_max = max([item.amount for item in exp])
    exp_min= min([item.amount for item in exp])
    inc_max = max([item.amount for item in inc])
    inc_min= min([item.amount for item in inc])

if len(exp) == 0:
    total_exp = 0
    exp_max = 0
    exp_min = 0
if len(inc) == 0:
    total_inc = 0
    inc_max = 0
    inc_min = 0
if len(pay) == 0:
    total_pay = 0

if total_inc >= total_exp:
    balance = total_inc - total_exp
    percentage = balance/total_inc * 100
else:
    balance = total_exp - total_inc
    percentage = balance/total_exp * 100
data = {
    "expense":exp,
    "incomes" : inc,
    "payment": pay,
    "total_exp" : total_exp,
    "total_inc" : total_inc,
    "total_pay" : total_pay,
    "exp_max" : exp_max,
    "exp_min" : exp_min,
    "inc_max":inc_max,
    "inc_min":inc_min,
    "balance":balance,
    "percentage": percentage,
}    

class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_pdf_main('base/report.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

