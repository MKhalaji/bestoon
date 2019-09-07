#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'submit/expense/',views.submit_expense,name="submit_expense"),
    path(r'submit/income/',views.submit_income,name="submit_income"),
]


#from django.contrib import admin
#from django.urls import path, include
