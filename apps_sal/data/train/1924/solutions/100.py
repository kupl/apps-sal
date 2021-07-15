class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        invalid_trans = set()
        d = {}
        for transaction in transactions:
            t_list = transaction.split(',')
            person, time, amount, loc = t_list[0], int(t_list[1]), int(t_list[2]), t_list[3]
            
            if amount > 1000:
                invalid_trans.add(transaction)
            
            if person not in d:
                d[person] = []
            else:
                for t in d[person]:
                    old_t = t.split(',')
                    old_time, old_loc = int(old_t[1]), old_t[3]
                    
                    if abs(old_time-time)<=60 and old_loc != loc:
                        invalid_trans.add(transaction)
                        invalid_trans.add(t)
            
            d[person].append(transaction)
            
        
        return list(invalid_trans)
