class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        
        for i in range(len(transactions) - 1):
            t1 = transactions[i].split(',')
            # transaction over $1000
            if int(t1[2]) > 1000:
                res.add(transactions[i])
            for j in range(i + 1, len(transactions)):
                t2 = transactions[j].split(',')
                # names match, cities do not match, transactions within 60 min
                if t1[0] == t2[0] and t1[3] != t2[3] and abs(int(t2[1]) - int(t1[1])) <= 60:
                    res.add(transactions[i])
                    res.add(transactions[j])
                if int(t2[2]) > 1000:
                    res.add(transactions[j])
                    
        return list(res)
                
                    
                
                
                

