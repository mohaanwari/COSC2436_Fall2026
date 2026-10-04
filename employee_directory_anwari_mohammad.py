# Review Programming Assignment
# Program Description: Read employee records, update the directory, save the
# updated records, and display a dictionary containing lists of employee data.
# Your Name: Mohammad Anwari
# Date: October 4, 2026


# Employee Class
class Employee:
    """Employee class to keep track of employee info."""

    def __init__(self, ID=-999, name='', department='', pay=0.0):
        """Initialize a new employee object."""
        self.set_ID(ID)
        self.set_name(name)
        self.set_department(department)
        self.set_pay(pay)

    # Getters and setters
    def get_ID(self):
        """Return employee ID."""
        return self.ID

    def set_ID(self, ID):
        """Assign employee ID."""
        self.ID = ID

    def get_name(self):
        """Return employee name."""
        return self.name

    def set_name(self, name):
        """Assign employee name."""
        self.name = name

    def get_department(self):
        """Return employee department."""
        return self.department

    def set_department(self, department):
        """Assign employee department."""
        self.department = department

    def get_pay(self):
        """Return employee pay."""
        return self.pay

    def set_pay(self, pay):
        """Assign employee pay."""
        self.pay = pay

    def __str__(self):
        """Return employee data as a tab-separated string."""
        return (f'{self.get_ID()}\t{self.get_name()}\t'
                f'{self.get_department()}\t{self.get_pay()}')


class EmployeeDirectory:
    """Track employee info in the directory."""

    def __init__(self):
        """Initialize employee_list and employee_dict."""
        self.employee_list = []
        self.employee_dict = {}

    def add_employee(self, employee):
        """Append an employee unless the ID is already in the directory."""
        # Check IDs because different objects can represent the same employee.
        for emp in self.employee_list:
            if emp.get_ID() == employee.get_ID():
                return
        self.employee_list.append(employee)

    def del_employee(self, employee):
        """Delete the employee with the matching ID, if found."""
        for emp in self.employee_list:
            if emp.get_ID() == employee.get_ID():
                self.employee_list.remove(emp)
                return
        print(f'ID:{employee.get_ID()} does not exist, deletion is aborted')

    def read_file(self, file_name):
        """Read employee records and return a list of Employee objects."""
        employees = []
        with open(file_name, 'r') as employee_file:
            for line in employee_file:
                # Skip blank lines and split each record into its four fields.
                if line.strip():
                    ID, name, department, pay = line.split()
                    emp = Employee(int(ID), name, department, float(pay))
                    employees.append(emp)
        return employees

    def update_employee_dir(self, file_name):
        """Read the file and update employee_list without duplicate IDs."""
        employees = self.read_file(file_name)
        self.employee_list = []
        for emp in employees:
            self.add_employee(emp)

    def write_to_file(self, file_name):
        """Overwrite the file with the updated employee_list."""
        with open(file_name, 'w') as employee_file:
            for emp in self.employee_list:
                employee_file.write(str(emp) + '\n')

    def write_to_dict(self):
        """Convert employee_list into a dictionary of attribute lists."""
        self.employee_dict = {'ID': [], 'name': [], 'department': [], 'pay': []}
        for emp in self.employee_list:
            self.employee_dict['ID'].append(emp.get_ID())
            self.employee_dict['name'].append(emp.get_name())
            self.employee_dict['department'].append(emp.get_department())
            self.employee_dict['pay'].append(emp.get_pay())

    def display_dict(self):
        """Display employee dictionary in key/value pairs."""
        for key, value in self.employee_dict.items():
            print(f'{key} : {value}')


# Test class
if __name__ == '__main__':
    try:
        directory = EmployeeDirectory()
        directory.update_employee_dir('employees.txt')

        # Create all three objects, but add only emp1 and emp2 as instructed.
        emp1 = Employee(106, 'Emp1', 'Accounting', 56000.0)
        emp2 = Employee(107, 'Emp2', 'Sales', 80000.0)
        emp3 = Employee(108, 'Emp3', 'Marketing', 90000.0)

        directory.add_employee(emp1)
        directory.add_employee(emp2)
        directory.del_employee(emp3)

        directory.write_to_file('employees.txt')
        directory.write_to_dict()
        directory.display_dict()
    except FileNotFoundError as fnfe:
        print(fnfe)
    except KeyError as ke:
        print(ke)
    except Exception as ex:
        print(ex)
    finally:
        print('Program is completed')
