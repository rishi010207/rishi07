class Add:
    a = 1 #First number 
    b = 2 #Second number
    
    def __init__(self):
        
        #Initialisation
        self.a=5
        self.b=10
        
    def calculate(self):
        
        #Calculation
        print("a=", self.a)
        print("b=", self.b)
        
        init_sum=(self.a+self.b)
        print("sum is",init_sum)
        
        print("a=",Add.a)
        print("b=",Add.b)
        class_sum=Add.a+Add.b
        
        print("sum is ", class_sum)

#Function calls
a1=Add()
a1.calculate()
               
