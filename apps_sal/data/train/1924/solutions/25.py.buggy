from collections import defaultdict
class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
    
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        trans_index = defaultdict(list)
        trans = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            trans.append(Transaction(name, time, amount, city))
        trans.sort(key = lambda x: x.time)
        
        s = set()
        for i in range(len(trans)):
            t1 = trans[i]
            if t1.amount > 1000:
                s.add(\"{},{},{},{}\".format(t1.name, t1.time, t1.amount, t1.city))
            for j in range(i + 1, len(trans)):
                t2 = trans[j]
                if t2.time - t2.time > 60:
                    break
                if t2.name == t1.name and t2.time - t1.time <= 60 and t1.city != t2.city:
                    s.add(\"{},{},{},{}\".format(t1.name, t1.time, t1.amount, t1.city))
                    s.add(\"{},{},{},{}\".format(t2.name, t2.time, t2.amount, t2.city))
        return list(s)
            
        
            
            
