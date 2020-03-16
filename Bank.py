class Bank(object):
    
    #Initialising variables
    name=""
    acctno=0
    initial_bal=0.0
    amt=0
    
    def accept(self):
        
        print("Welcome to ABC bank")
        print("   ")
        print("Please Enter your Name!")
        
        self.name=input("Enter your Name = ")
        self.acctno=int(input("Enter your Account No. = "))
        self.initial_bal=5000
        
        print("YOUR BALANCE IS = ",self.initial_bal)
        print("Customer Details")
        print("Nme= ",self.name,"                Account No. = ",self.acctno) 
        print("Current Balance = ",self.initial_bal)

        
    def deposit(self):
        
        print("Enter amount to be deposited")
        self.amt = int(input())
        self.initial_bal=self.initial_bal+self.amt
        print("Update balance is",self.initial_bal)

        
    def withdraw(self):       
        print("Enter amount to be withdraw")
        self.amt = int(input())
        self.initial_bal=self.initial_bal-self.amt
        print("Updated balance is",self.initial_bal)
        

#Function calling
b1=Bank()
b1.accept()
b1.deposit()
b1.withdraw()
