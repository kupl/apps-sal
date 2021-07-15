class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    #Happy coding
    def withdraw(self, money):
        if self.balance < money:
            raise ValueError
        self.balance -= money
        return f'{self.name} has {self.balance}.'
    def check(self, user, money):
        user.withdraw(money)
        if not user.checking_account: 
            raise ValueError
        self.balance += money
        return f'{self.name} has {self.balance} and {user.name} has {user.balance}.'
    def add_cash(self, money):
        self.balance += money
        return f'{self.name} has {self.balance}.'
