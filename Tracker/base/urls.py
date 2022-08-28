from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

app_name = 'tracker'

urlpatterns = [
    path('', views.home, name="home"),
    path('expenses/', views.expenses_data, name="expenses"),
    #path('form1/', views.expense_form, name="form1"),
    path('classes/',views.classes, name="class"),
    path('classes_form', views.new_class, name="class_form"),
    path('update_class/<str:pk>/', views.update_class, name="update_class"),
    path('delete_class/<str:pk>/', views.delete_class, name="delete_class"),
    path('payment', views.payment, name='payment'),
    path('payment_form/', views.new_payment, name='payment_form'),
    path('payment_update/<str:pk>', views.payment_update, name="payment_update"),
    path('delete_payment/<str:pk>/', views.payment_delete, name="payment_delete"),
    path('expense_form/', views.new_expense, name='expense_form'),
    path('update_expense/<str:pk>/', views.update_expense, name="update_expense"),
    path('expense_delete/<str:pk>/', views.expense_delete, name="expense_delete"),
    path('incomes/', views.income_detail, name="incomes"),
    path('income_form/', views.new_income, name="income_form"),
    path('income_update/<str:pk>/', views.update_income, name="update_income"),
    path('income_delete/<str:pk>/', views.income_delete, name='delete_income'),
    path('items/', views.items, name="items"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('register/', views.register_page, name="register"),
    path("login/", views.login_page, name="login"),
    
]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)