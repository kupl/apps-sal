class Transactions: 
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = time
        self.amount = amount
        self.city = city 

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transact = []
        for t in transactions:
            t = t.split(',')
            obj = Transactions(t[0], int(t[1]), int(t[2]), t[3])
            transact.append(obj)
        transact.sort(key=lambda t: t.time)
        invalid = set() 
        for i in range(len(transact)):
            first = transact[i]
            if first.amount > 1000:
                invalid.add(self.returnString(first))
            for j in range(i+1, len(transact)):
                second = transact[j]
                if first.name == second.name and first.city != second.city and second.time - first.time <= 60:
                    invalid.add(self.returnString(first))
                    invalid.add(self.returnString(second))
                    
        return list(invalid)
    
    def returnString(self, first):
        return first.name + ',' + str(first.time) + ',' + str(first.amount) + ',' + first.city

