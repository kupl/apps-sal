class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    #Happy coding
    def withdraw(self, wd):
        if not wd > self.balance:
            self.balance -= wd 
            return f"{self.name} has {self.balance}."
        raise (f"{self.name} can't withdraw {wd}, he only has {self.balance}.")
        
    def check(self , other, dd):
        if other.checking_account:
             if dd > other.balance:
                 raise ValueError
             self.balance += dd
             other.balance -= dd
             return  f"{self.name} has {self.balance} and {other.name} has {other.balance}."
        raise ( f"{other.name} doesn't have enough money.")
        
    def add_cash(self , ad):
        self.balance += ad 
        return f"{self.name} has {self.balance}."
