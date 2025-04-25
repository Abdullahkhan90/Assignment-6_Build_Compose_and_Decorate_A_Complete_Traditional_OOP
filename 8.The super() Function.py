class Person:  
    def __init__(self, name):  
        self.name = name  

class Teacher(Person):  
    def __init__(self, name, subject):  
        super().__init__(name)   
        self.subject = subject  

t = Teacher("Ahmed", "Mathematics")  
print(f"Teacher Name: {t.name}")  
print(f"Subject: {t.subject}")  