from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        if not transactions:
            return []
        
        d = defaultdict(list)
        result = set()
        
        for i in range(len(transactions)):
            name, time, amount, city = (int(i) if i.isnumeric() else i for i in transactions[i].split(\",\"))
            
            if amount > 1000:
                result.add(transactions[i])
                
            if name in d:
                for tran in d[name]:
                    _, prev_time, _, prev_city = (int(i) if i.isnumeric() else i for i in tran.split(\",\"))
                    if abs(time - prev_time) <= 60 and prev_city != city:
                        result.add(tran)
                        result.add(transactions[i])
            
            d[name].append(transactions[i])
        
        return result

