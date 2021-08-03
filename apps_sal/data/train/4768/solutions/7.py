
class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError
        self.balance -= amount
        return "{} has {}.".format(self.name, self.balance)

    def check(self, other, amount):
        if amount > other.balance or not other.checking_account:
            raise ValueError
        other.balance -= amount
        self.balance += amount
        return ("{} has {} and {} has {}."
                .format(self.name, self.balance, other.name, other.balance))

    def add_cash(self, amount):
        self.balance += amount
        return "{} has {}.".format(self.name, self.balance)
