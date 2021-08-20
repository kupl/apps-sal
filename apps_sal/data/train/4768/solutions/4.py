class User(object):

    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = int(balance)
        self.checking_account = checking_account

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError
        self.balance = int(self.balance - amount)
        return f'{self.name} has {self.balance}.'

    def check(self, other, amount):
        if not other.checking_account or amount > other.balance:
            raise ValueError
        other.balance = int(other.balance - amount)
        self.balance = int(self.balance + amount)
        return f'{self.name} has {self.balance} and {other.name} has {other.balance}.'

    def add_cash(self, amount):
        self.balance = int(self.balance + amount)
        return f'{self.name} has {self.balance}.'
