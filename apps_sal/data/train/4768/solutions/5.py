class User(object):

    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            raise ValueError
        return f'{self.name} has {self.balance}.'

    def check(self, other, amount):
        if not other.checking_account:
            raise ValueError
        if other.balance > amount:
            other.balance -= amount
            self.balance += amount
        else:
            raise ValueError
        return f'{self.name} has {self.balance} and {other.name} has {other.balance}.'

    def add_cash(self, amount):
        self.balance += amount
        return f'{self.name} has {self.balance}.'
