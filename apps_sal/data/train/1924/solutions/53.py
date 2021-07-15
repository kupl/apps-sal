import collections
import bisect

class Solution:
    def invalidTransactions(self, orig: List[str]) -> List[str]:
        transactions = collections.defaultdict(lambda: [])
        
        for idx, t in enumerate(orig):
            name, time, amount, city = t.split(\",\")
            
            time = int(time)
            amount = int(amount)
            
            bisect.insort(transactions[name], [time, amount, city, idx])
            
        invalid_transactions = set([])
        
        for name in transactions:
            lst = transactions[name]
            lst = sorted(lst, key = lambda item: item[0])
            
            for idx in range(len(lst)):
                t1, a1, c1, i1 = lst[idx]
                
                if a1 > 1000:
                    invalid_transactions.add(i1)
                
                for idy in range(idx + 1, len(lst)):
                    if idx == idy:
                        continue
                        
                    t2, a2, c2, i2 = lst[idy]
                    
                    if (t2 - t1) <= 60 and c1 != c2:
                        invalid_transactions.add(i1)
                        invalid_transactions.add(i2)
                    elif (t2 - t2) > 60:
                        break
                        
        ret = []
        for index in invalid_transactions:
            ret.append(orig[index])
            
        return ret
                    
