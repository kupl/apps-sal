class Transaction(object):
    def __init__(self, txn):
        name, time, amount, city = txn.split(',')
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
        
    def __str__(self):
        return \"{},{},{},{}\".format(self.name, self.time, self.amount, self.city)
    
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        d = defaultdict(list)
        ans = []
        txns = list(map(Transaction, transactions))
        for i, t in enumerate(txns):
            d[t.name].append(i)
        for name, tid in d.items():    
            l = r = 0
            for t in (tid := sorted(tid, key=lambda x:txns[x].time)):
                if txns[t].amount > 1000:
                    ans.append(t)
                    continue
                while l + 1 < len(tid) and txns[tid[l]].time + 60 < txns[t].time:
                    l += 1
                while r + 1 < len(tid) and txns[tid[r+1]].time <= txns[t].time + 60:
                    r += 1
                for j in range(l, r+1):
                    if txns[tid[j]].city != txns[t].city:
                        ans.append(t)
                        break
        return [str(transactions[i]) for i in ans]      
