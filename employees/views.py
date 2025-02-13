from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
import pandas as pd
import os

def home(request):
    return render(request, 'home.html')

def save_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to a list of employees or another appropriate view
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def search_employee(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(first_name__icontains=query)  # Example search by first name
    else:
        employees = Employee.objects.all()  # Return all employees if no query is provided
    return render(request, 'employee_list.html', {'employees': employees})