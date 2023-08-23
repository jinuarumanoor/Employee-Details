from django.http import HttpResponse
from django.shortcuts import render
from Employees.models import Employee

def Home(request):
    employees = Employee.objects.all()
    context={
        'employees':employees,
        }
    return render(request, 'home.html',context)
