from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        previous = defaultdict(list)
        ans = set()
        
        for transaction in transactions:
            
            
            name, time, amount, city = (int(i) if i.isnumeric() else i for i in transaction.split(','))
            
            if amount > 1000:
                ans.add(transaction)
                
            for tran in previous[name]:
                _, prev_time, _, prev_city = (int(i) if i.isnumeric() else i for i in tran.split(','))
                
                if abs(time - prev_time) <= 60 and city != prev_city:
                    ans.add(tran)
                    ans.add(transaction)
            previous[name].append(transaction)
        return ans
                
                                            

