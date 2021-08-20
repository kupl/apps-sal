class User(object):

    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, v):
        if v > self.balance:
            raise ValueError()
        self.balance -= v
        return '{} has {}.'.format(self.name, int(self.balance))

    def add_cash(self, v):
        self.balance += v
        return '{} has {}.'.format(self.name, int(self.balance))

    def check(self, other, v):
        if not other.checking_account:
            raise ValueError()
        (s1, s2) = (other.withdraw(v), self.add_cash(v)[:-1])
        return '{} and {}'.format(s2, s1)

    def __str__(self):
        return 'User({}, {}, {})'.format(self.name, self.balance, self.checking_account)
