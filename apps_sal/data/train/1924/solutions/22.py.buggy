class Transaction:
    
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
        
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
            
        tr = [Transaction(*t.split(',')) for t in transactions]
        transactions = sorted(tr, key=lambda x : x.time)
        
        invalid = set()
        for t in transactions:
            if t.amount > 1000:
                invalid.add(\"{},{},{},{}\".format(t.name, t.time, t.amount, t.city))
            for o in transactions:
                if t.name == o.name and abs(t.time - o.time) <= 60 and t.city != o.city:
                    invalid.add(\"{},{},{},{}\".format(t.name, t.time, t.amount, t.city))
                    invalid.add(\"{},{},{},{}\".format(o.name, o.time, o.amount, o.city))
        return list(invalid)
