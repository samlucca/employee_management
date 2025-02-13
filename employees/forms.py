from django import forms
from .models import Employee
import datetime

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'new_employee_code', 'old_employee_code', 'sap_code', 'first_name', 'surname', 
            'gender', 'date_of_joining', 'date_of_birth', 'department', 'cost_centre_code', 
            'designation_code', 'designation', 'reporting_hod_emp_code', 'reporting_hod', 
            'reporting_designation', 'contact_no', 'location', 'unit', 'unit_code', 
            'marital_status', 'religion', 'highest_education', 'permanent_address', 
            'current_address', 'status', 'grade', 'last_medical_date', 'locker_no', 
            'eligibility_for_shoes', 'esic_eligibility', 'esic_number', 'pf_number', 
            'pf_account_no', 'pf_uan_number', 'bank', 'bank_account_number', 
            'aadhaar_card', 'pan_card', 'employee_type', 'contractor_name', 'contractor_code'
        ]

    def clean_date_of_joining(self):
        date_of_joining = self.cleaned_data.get('date_of_joining')
        if date_of_joining > datetime.date.today():
            raise forms.ValidationError("Date of Joining cannot be in the future.")
        return date_of_joining

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth > datetime.date.today():
            raise forms.ValidationError("Date of Birth cannot be in the future.")
        return date_of_birth

    def clean_contact_no(self):
        contact_no = self.cleaned_data.get('contact_no')
        if not contact_no.isdigit() or len(contact_no) != 10:
            raise forms.ValidationError("Contact No. must be a 10-digit number.")
        return contact_no

    def clean_aadhaar_card(self):
        aadhaar_card = self.cleaned_data.get('aadhaar_card')
        if not aadhaar_card.isdigit() or len(aadhaar_card) != 12:
            raise forms.ValidationError("Aadhaar Card must be a 12-digit number.")
        return aadhaar_card

    def clean_pan_card(self):
        pan_card = self.cleaned_data.get('pan_card')
        if len(pan_card) != 10:
            raise forms.ValidationError("PAN Card must be a 10-character string.")
        return pan_card

    def clean_employee_type(self):
        employee_type = self.cleaned_data.get('employee_type')
        if employee_type not in ['Staff', 'Worker']:
            raise forms.ValidationError("Employee Type must be either 'Staff' or 'Worker'.")
        return employee_type

    # Additional validation methods can be added for other fields as needed.