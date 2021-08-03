class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        list_transactions = []
        hash = defaultdict(list)
        for i, t in enumerate(transactions):
            temp = t.split(\",\")
            temp.append(i)
            list_transactions.append(temp)
            
        for i in range(len(list_transactions)):
            t1 = list_transactions[i]
            if int(t1[2]) > 1000:
                res.add(transactions[i])
            
            if t1[0] in hash:
                for t2 in hash[t1[0]]:
                    if t2[3] != t1[3] and abs(int(t1[1]) - int(t2[1])) <= 60:
                        res.add(transactions[t2[4]])
                        res.add(transactions[i])
            hash[t1[0]].append(t1)

                    
        return list(res)
                
                    
                
                
                
        
