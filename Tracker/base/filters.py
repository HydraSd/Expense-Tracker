import django_filters
from django_filters import DateFilter,CharFilter
from matplotlib import widgets
from django import forms

from .models import *

class PaymentFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr='lte')
    note = CharFilter(field_name='description', lookup_expr='icontains')
    class Meta:
        model = Payment
        fields = ["class_name","amount"]
        # exclude = ["class_name", "date", "amount", "description"]
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'Type': forms.Select(attrs={'class':'form-control'}),
            'detail': forms.TextInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control'})
        }

class ExpenseFilter(django_filters.FilterSet):
    # gte = greater than or equal
    # lte = less than or equal
    start_date = DateFilter(field_name="date", lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    note = CharFilter(field_name="detail", lookup_expr='icontains')
    class Meta:
        model = Expense
        fields = ["Type", "amount"]

class IncomeFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr='lte')
    note = CharFilter(field_name="income_detail", lookup_expr="icontains")
    class Meta:
        model = Income
        fields = ["income_ty", "amount"]

class DateFill(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr='lte')
    class Meta:
        model: Income


        