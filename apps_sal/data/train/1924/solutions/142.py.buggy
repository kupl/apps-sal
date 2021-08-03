class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [ x.split(\",\") for x in transactions]
        transactions =[ [x[0],int(x[1]),int(x[2]),x[3]] for x in transactions]
        transactions.sort(key=lambda x:x[1])
        res=set()
        n=len(transactions)
        for i in range(n):
            nam1,tim1,amt1,city1=transactions[i]
            
            if int(amt1)>1000:
                res.add(f\"{nam1},{tim1},{amt1},{city1}\")
            for j in range(i+1,n):
                nam2,tim2,amt2,city2=transactions[j]
                if nam1==nam2 and int(tim2)-int(tim1)<=60 and city1!=city2:
                    res.add(f\"{nam1},{tim1},{amt1},{city1}\")
                    res.add(f\"{nam2},{tim2},{amt2},{city2}\")
        return list(res)
                
                
                
            
            
