## Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:  
    @staticmethod  
    def add(a, b):  
        return a + b  

result = MathUtils.add(9, 19)  
print("Sum of my Two Numbers are:", result)  