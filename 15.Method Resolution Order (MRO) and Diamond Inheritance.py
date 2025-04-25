## Create four classes:

''' A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO ''' 

class A:
    def show(self):
        print("Show method from Class A")

class B(A):
    def show(self):
        print("Show method from Class B")
        super().show()

class C(A):
    def show(self):
        print("Show method from Class C")
        super().show()

class D(B, C):
    def show(self):
        print("Show method from Class D")
        super().show()


d = D()
d.show()

print("\nMethod Resolution Order (MRO):")
for cls in D.__mro__:
    print(cls)
