from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.shortcuts import get_object_or_404
from Employees.models import Employee
# Create your views here.
def employee_detail(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    return render(request,'employee_detail.html',{'employee':employee})
   
   