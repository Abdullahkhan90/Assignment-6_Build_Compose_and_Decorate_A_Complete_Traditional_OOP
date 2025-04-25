## Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:  
    def __init__(self, name):  
        self.name = name  

class Department:  
    def __init__(self, name):  
        self.name = name  
        self.employees = []  
    
    def add_employee(self, employee):  
        self.employees.append(employee)   

    def list_employees(self):  
        for emp in self.employees:  
            print(emp.name)  


emp1 = Employee("Saad")  
emp2 = Employee("Faiq")  

dept = Department("HR")  
dept.add_employee(emp1)  
dept.add_employee(emp2)  

print(f"Employees in {dept.name} department:")  
dept.list_employees()  