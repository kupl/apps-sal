class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        from collections import defaultdict
        newd =defaultdict(list)
        result =set()
        for j in range(len(transactions)):
            details = transactions[j].split(\",\")
            
            if int(details[2])>1000:
                result.add(transactions[j])
                
            if newd[details[0]]:
                
                for tran in newd[details[0]]:
                    name, time,amount,city = tuple(tran.split(\",\"))
                    if abs(int(details[1])-int(time))<=60 and details[3]!=city:
                        result.add(transactions[j])
                        result.add(tran)
            
            
            newd[details[0]].append(transactions[j])

        
        return result
