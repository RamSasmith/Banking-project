class Account:
    def __init__(self, number, customer, kind, balance=0):
        self.number, self.customer, self.kind = number, customer, kind
        self.balance = float(balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Enter a valid amount")
        self.balance += amount

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0 or amount > self.balance:
            raise ValueError("Insufficient balance or invalid amount")
        self.balance -= amount

class SavingsAccount(Account):
    def withdraw(self, amount):
        if self.balance - float(amount) < 500:
            raise ValueError("Keep at least ₹500 in savings account")
        super().withdraw(amount)

class CurrentAccount(Account):
    pass
