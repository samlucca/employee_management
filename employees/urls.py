
from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line for the root path
    path('save/', views.save_employee, name='save_employee'),
    path('search/', views.search_employee, name='search_employee'),
    path('import_excel/', views.import_excel, name='import_excel'),  # Add this line for importing Excel files
]