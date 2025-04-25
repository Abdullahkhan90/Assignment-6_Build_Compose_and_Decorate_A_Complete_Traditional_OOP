class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

m = Multiplier(5)


print("Is m callable?", callable(m))  

result = m(10)
print("Result of calling m(10):", result)  
