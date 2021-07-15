class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = time
        self.amount = amount
        self.city = city

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        def formatRes(t):
            return \"{},{},{},{}\".format(t.name, t.time, t.amount, t.city)
        l = []
        res = set()
        for transaction in transactions:
            name, time, amount, city = transaction.split(\",\")
            l.append(Transaction(name, int(time), int(amount), city))
        l.sort(key=lambda t: t.time)
        
        for i in range(len(l)):
            t1 = l[i]
            if t1.amount > 1000:
                res.add(formatRes(t1))
            for j in range(i+1, len(l)):
                t2 = l[j]
                if t1.name == t2.name and t2.time-t1.time <= 60 and t2.city != t1.city:
                    res.add(formatRes(t1))
                    res.add(formatRes(t2))
        res = list(res)
        return res
