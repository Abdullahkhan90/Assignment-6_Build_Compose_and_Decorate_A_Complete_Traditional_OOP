class Logger:  
    def __init__(self):  
        print("Message Before: Logger Object Created.")  

    def __del__(self):  
        print("Message After: Logger Object Destructor.")  

log = Logger()  

del log        