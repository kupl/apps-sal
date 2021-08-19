class User(object):

    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money):
        if self.balance < money:
            raise ValueError
        self.balance -= money
        return self.name + ' has ' + str(self.balance) + '.'

    def check(self, other, money):
        if other.balance < money:
            raise ValueError
        if not other.checking_account:
            raise ValueError
        other.balance -= money
        self.balance += money
        return self.name + ' has ' + str(self.balance) + ' and ' + other.name + ' has ' + str(other.balance) + '.'

    def add_cash(self, money):
        self.balance += money
        return self.name + ' has ' + str(self.balance) + '.'
