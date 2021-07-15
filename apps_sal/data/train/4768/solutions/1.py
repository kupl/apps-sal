class User:
    def __init__(self, name, balance, checking_account):
        self.name, self.balance, self.checking_account = name, balance, checking_account
    def __str__(self):
        return "{} has {:d}.".format(self.name, self.balance)
    def withdraw(self, amount):
        if self.balance < amount: raise ValueError("Not enough money.")
        self.balance -= amount
        return str(self)
    def add_cash(self, amount):
        self.balance += amount
        return str(self)
    def check(self, other, amount):
        if not other.checking_account:
            raise ValueError("Can't transfer money from this account.")
        other.withdraw(amount)
        self.add_cash(amount)
        return "{} and {}".format(str(self)[:-1], other)
