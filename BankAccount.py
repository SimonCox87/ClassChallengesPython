class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
    
    def withdrawal(self, amount):
        self.amount = amount
        self.balance -= self.amount

    def bankFees(self, fee = 5):
        self.fee = fee
        fee = self.balance * (fee / 100)
        self.balance -= fee
    
    def display(self):
        return f'Account Number: {self.accountNumber}\nName: {self.name}\nBalance: {self.balance}'
    
accountHolder = BankAccount(999999, "Fred Bloggs", 100.0)
print(accountHolder.display())
accountHolder.deposit(10)
print(accountHolder.display())
accountHolder.bankFees()
print(accountHolder.display())
