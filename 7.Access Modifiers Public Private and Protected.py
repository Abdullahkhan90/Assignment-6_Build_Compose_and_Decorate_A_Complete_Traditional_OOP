class Employee:  
    def __init__(self, name, salary, ssn):  
        self.name = name          # Public variable  
        self._salary = salary     # Protected variable 
        self.__ssn = ssn          # Private variable 

# Create an object of Employee  
emp = Employee("Abdullah", 50000, "123-45-6789")  

# Accessing public variable  
print("Name (public):", emp.name)   

# Accessing protected variable  
print("Salary (protected):", emp._salary) 
print("SSN (private):", emp._Employee__ssn)  