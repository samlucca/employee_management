from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('save/', views.save_employee, name='save_employee'),  # Save employee
    path('search/', views.search_employee, name='search_employee'),  # Search employee
    path('import_excel/', views.import_excel, name='import_excel'),  # Import Excel file
    path('export_excel/', views.export_excel, name='export_excel'),  # Export Excel file
    path('employee_list/', views.employee_list, name='employee_list'),  # View all employees
]