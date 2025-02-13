# Employee Management App

This project is an Employee Management Application developed using Python and Django. It allows for the management of employee records, including the ability to perform CRUD (Create, Read, Update, Delete) operations. The application features a user-friendly interface for entering employee details and includes validation for all required fields.

## Features

- Employee Form: A comprehensive form to input employee details with validation.
- CRUD Operations: Create, read, update, and delete employee records.
- Excel Integration: Import and export employee data to and from Excel files.
- Search Functionality: Search for employees by name, employee code, or SAP code.

## Project Structure

```
employee-management-app
├── employee_management
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── templates
│       └── employee_form.html
├── employees
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd employee-management-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.
- Use the employee form to add new employee records.
- Utilize the search functionality to find existing employees.
- Import and export employee data using Excel files.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.