class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ts = []
        for t in transactions:
            name, stamp, amount, city = t.split(\",\")
            ts.append([name, int(stamp), int(amount), city, t])
        
        s = set()
        
        for t in ts:
            if t[2] > 1000: s.add(t[4])
            for v in ts:
                if t[0] == v[0] and abs(t[1] - v[1]) <= 60 and t[3] != v[3]: s.add(v[4])
    
        return list(s)
