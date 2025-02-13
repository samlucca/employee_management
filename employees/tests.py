from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):

    def setUp(self):
        Employee.objects.create(
            new_employee_code='36195',
            old_employee_code='22546',
            sap_code='34434',
            first_name='DIPTESH',
            surname='NAIK',
            gender='M',
            date_of_joining='2021-04-01',
            date_of_birth='1988-07-08',
            department='TUFFTING SMI-1',
            cost_centre_code='1805',
            designation='PRODUCTION HELPER',
            reporting_hod_emp_code='LEONARD',
            contact_no='1234567890',
            location='SMI',
            marital_status='Single',
            religion='Hindu',
            highest_education='Graduate',
            permanent_address='123 Main St',
            current_address='456 Elm St',
            status='Active',
            grade='GR-2',
            last_medical_date='2023-01-01',
            locker_no='A1',
            esic_eligibility='Yes',
            esic_number='ESIC123456',
            pf_number='PF123456',
            pf_account_no='PFACC123456',
            pf_uan_number='UAN123456',
            bank='Bank of Test',
            bank_account_number='BANKACC123456',
            aadhar_card='AADHAR123456',
            pan_card='PAN123456',
            employee_type='Staff',
            contractor_name='ATHARAV SERVICES',
            contractor_code='CONTRACTOR123'
        )

    def test_employee_creation(self):
        employee = Employee.objects.get(new_employee_code='36195')
        self.assertEqual(employee.first_name, 'DIPTESH')
        self.assertEqual(employee.surname, 'NAIK')
        self.assertEqual(employee.gender, 'M')
        self.assertEqual(employee.department, 'TUFFTING SMI-1')

    def test_employee_search_by_name(self):
        response = self.client.get('/employees/search/', {'query': 'DIPTESH'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'DIPTESH')

    def test_employee_search_by_code(self):
        response = self.client.get('/employees/search/', {'query': '36195'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'DIPTESH')

    def test_employee_search_by_sap_code(self):
        response = self.client.get('/employees/search/', {'query': '34434'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'DIPTESH')