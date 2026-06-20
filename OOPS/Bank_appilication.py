import sys
class customer:
    bank_name= "SBI"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def Deposite(self,amount):
        self.amount=amount
        self.balance=self.balance+amount
        print(f"balance after deposite is : {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"Insufficient funds....please check your balance")
            sys.exit()
        elif amount<=0:
            print("Your Enter the  incorrect amount.........Please enter the current amount")
            sys.exit()
        self.balance=self.balance-amount
        print(f"balance after withdraw........ your funds is : {self.balance}")
    def check_bal(self):
        print(f"Your Account funds is:{self.balance} ")

    def create_pin(self):
        print("this service is under development......... Please select another options")

print(f"Welcome to the {customer.bank_name}")
name=input("enter the customer name :").isupper()
c=customer(name)
while True:
    print("D- diposite \nW-withdraw\nb-balance\nP-pin Generation\nE-exit")
    option =input("please select option : ")
    if option =="D" or option=="d":
        amount = float(input("enter the deposite amount:"))
        c.Deposite(amount)

    elif option=='w' or option=='W':
        amount=float(input("enter the withdraw amount:"))
        c.withdraw(amount)
    elif option=='e' or option=='E':
        print("Thank you banking")
        break
    elif option=='b' or option=='B':
        c.check_bal()
    elif option=='p' or option=='P':
        c.create_pin()
    else:
        print("invilid option............Please select the correct option")  

