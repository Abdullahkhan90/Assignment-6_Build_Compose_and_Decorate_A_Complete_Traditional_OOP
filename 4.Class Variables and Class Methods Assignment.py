## Create a class Bank with a class variable bank_name. 

class Bank:  
    bank_name = "Askari Bank"  

    def __init__(self, account_holder):  
        self.account_holder = account_holder  

    @classmethod  
    def change_bank_name(cls, name):  
        cls.bank_name = name  

    def display(self):  
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")  

account1 = Bank("Abdullah")  
account2 = Bank("Ahmed")  

account1.display()  
account2.display()  

Bank.change_bank_name("Meezan Bank")  

account1.display()  
account2.display()   