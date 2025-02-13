from django.shortcuts import render, redirect
from django.http import HttpResponse
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
            employee = form.save()
            # Append the employee details to the existing Excel file
            file_path = 'path/to/your/existing/excel/file.xlsx'  # Update this path
            if os.path.exists(file_path):
                df = pd.read_excel(file_path)
                new_data = {
                    'Sr. nos.': employee.sr_no,
                    'New Employee Code': employee.new_employee_code,
                    'Old Employee Code': employee.old_employee_code,
                    'SAP code': employee.sap_code,
                    'First Name': employee.first_name,
                    'Surname': employee.surname,
                    'Gender(M.F.T)': employee.gender,
                    'Date of Joining(DD-MM-YYYY)': employee.date_of_joining,
                    'Date of Birth(DD-MM-YYYY)': employee.date_of_birth,
                    'Department': employee.department,
                    'Cost Centre Code': employee.cost_centre_code,
                    'Designation': employee.designation,
                    'Designation Code': employee.designation_code,
                    'Reporting HOD emp Code': employee.reporting_hod_emp_code,
                    'Reporting HOD': employee.reporting_hod,
                    'Reporting designation': employee.reporting_designation,
                    'Contact No.': employee.contact_no,
                    'LOCATION': employee.location,
                    'UNIT': employee.unit,
                    'Unit Code': employee.unit_code,
                    'Marital Status': employee.marital_status,
                    'Religion': employee.religion,
                    'Highest Education': employee.highest_education,
                    'Permanent Address': employee.permanent_address,
                    'Current Address': employee.current_address,
                    'Status': employee.status,
                    'Grade': employee.grade,
                    'Last Medical date': employee.last_medical_date,
                    'Locker no.': employee.locker_no,
                    'Eligibility for Shoes.sandal.Chappal': employee.eligibility_for_shoes,
                    'ESIC Eligibility (Yes.No)': employee.esic_eligibility,
                    'ESIC Number': employee.esic_number,
                    'P.F. Number': employee.pf_number,
                    'P.F. Account No.': employee.pf_account_no,
                    'P.F. UAN NUMBER': employee.pf_uan_number,
                    'Bank': employee.bank,
                    'BANK ACCOUNT NUMBER': employee.bank_account_number,
                    'Aadhar Card': employee.aadhaar_card,
                    'Pan Card': employee.pan_card,
                    'Employee Type( Staff.worker)': employee.employee_type,
                    'CONTRACTOR NAME': employee.contractor_name,
                    'CONTRACTOR CODE': employee.contractor_code,
                }
                df = df.append(new_data, ignore_index=True)
                df.to_excel(file_path, index=False)
            else:
                # If the file does not exist, create a new one with the employee details
                new_data = {
                    'Sr. nos.': [employee.sr_no],
                    'New Employee Code': [employee.new_employee_code],
                    'Old Employee Code': [employee.old_employee_code],
                    'SAP code': [employee.sap_code],
                    'First Name': [employee.first_name],
                    'Surname': [employee.surname],
                    'Gender(M.F.T)': [employee.gender],
                    'Date of Joining(DD-MM-YYYY)': [employee.date_of_joining],
                    'Date of Birth(DD-MM-YYYY)': [employee.date_of_birth],
                    'Department': [employee.department],
                    'Cost Centre Code': [employee.cost_centre_code],
                    'Designation': [employee.designation],
                    'Designation Code': [employee.designation_code],
                    'Reporting HOD emp Code': [employee.reporting_hod_emp_code],
                    'Reporting HOD': [employee.reporting_hod],
                    'Reporting designation': [employee.reporting_designation],
                    'Contact No.': [employee.contact_no],
                    'LOCATION': [employee.location],
                    'UNIT': [employee.unit],
                    'Unit Code': [employee.unit_code],
                    'Marital Status': [employee.marital_status],
                    'Religion': [employee.religion],
                    'Highest Education': [employee.highest_education],
                    'Permanent Address': [employee.permanent_address],
                    'Current Address': [employee.current_address],
                    'Status': [employee.status],
                    'Grade': [employee.grade],
                    'Last Medical date': [employee.last_medical_date],
                    'Locker no.': [employee.locker_no],
                    'Eligibility for Shoes.sandal.Chappal': [employee.eligibility_for_shoes],
                    'ESIC Eligibility (Yes.No)': [employee.esic_eligibility],
                    'ESIC Number': [employee.esic_number],
                    'P.F. Number': [employee.pf_number],
                    'P.F. Account No.': [employee.pf_account_no],
                    'P.F. UAN NUMBER': [employee.pf_uan_number],
                    'Bank': [employee.bank],
                    'BANK ACCOUNT NUMBER': [employee.bank_account_number],
                    'Aadhar Card': [employee.aadhaar_card],
                    'Pan Card': [employee.pan_card],
                    'Employee Type( Staff.worker)': [employee.employee_type],
                    'CONTRACTOR NAME': [employee.contractor_name],
                    'CONTRACTOR CODE': [employee.contractor_code],
                }
                df = pd.DataFrame(new_data)
                df.to_excel(file_path, index=False)
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

def import_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        file_path = 'path/to/your/existing/excel/file.xlsx'  # Update this path
        if os.path.exists(file_path):
            existing_df = pd.read_excel(file_path)
            combined_df = pd.concat([existing_df, df], ignore_index=True)
            combined_df.to_excel(file_path, index=False)
        else:
            df.to_excel(file_path, index=False)
        return redirect('home')
    return render(request, 'home.html')

def export_excel(request):
    file_path = 'path/to/your/existing/excel/file.xlsx'  # Update this path
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=employee_data.xlsx'
        df.to_excel(response, index=False)
        return response
    else:
        return HttpResponse("No data to export.")

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})