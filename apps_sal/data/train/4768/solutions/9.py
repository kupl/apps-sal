class User(object):

    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            return f'{self.name} has {self.balance}.'
        else:
            raise ValueError

    def check(self, other, money):
        if money <= other.balance and other.checking_account == True:
            other.balance -= money
            self.balance += money
            return f'{self.name} has {self.balance} and {other.name} has {other.balance}.'
        else:
            raise ValueError

    def add_cash(self, money):
        self.balance += money
        return f'{self.name} has {self.balance}.'
