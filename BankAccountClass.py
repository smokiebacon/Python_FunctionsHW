class BankAccount():
    def __init__(self, ownerName, balance):
        self.ownerName = ownerName
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough funds to withdraw')
        else:
            self.balance -= amount

account = BankAccount('Abe', 1000)
print(account.ownerName, account.balance)

account.withdraw(999)
print(account.ownerName, account.balance)

class CheckingAccount(BankAccount)
    def __init__(self):
        BankAccount.__init__(self)

class SavingAccount(BankAccount)
    def __init__(self):
        BankAccount.__init__(self)
