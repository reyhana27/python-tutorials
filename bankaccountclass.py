class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        
    def deposit(self, amount):
        if amount <= 0:
            print("the amount cannot be negative or equal to zero")
        elif amount > 0:
            self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("the amount you put is more than you can withdraw")
        elif amount <= self.balance:
            self.balance -= amount
    
    def showBalance(self):
        print(self.balance)
        
bankacc1 = BankAccount("Bob")
bankacc2 = BankAccount("Job")

bankacc1.deposit(400)
bankacc1.withdraw(200)
bankacc1.showBalance()

bankacc2.deposit(700)
bankacc2.withdraw(700)
bankacc2.showBalance()
    
        
        
        
        
        
