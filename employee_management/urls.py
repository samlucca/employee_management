from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line for the root path
    path('save/', views.save_employee, name='save_employee'),
    path('search/', views.search_employee, name='search_employee'),
]