from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('new_employee_code', 'first_name', 'surname', 'gender', 'date_of_joining', 'department', 'designation', 'contact_no')
    search_fields = ('first_name', 'new_employee_code', 'sap_code')

admin.site.register(Employee, EmployeeAdmin)