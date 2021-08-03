class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        s = set()
        for i in range(0,len(transactions)):
            name,time,amount,city = transactions[i].split(\",\")
            if int(amount) > 1000:
                s.add(transactions[i])
            for j in range(i+1,len(transactions)):
                name1,time1,amount1,city1 = transactions[j].split(\",\")
        
                if name == name1 and abs(int(time)-int(time1))<=60 and city!=city1:
                
                    s.add(transactions[i])
                    s.add(transactions[j])
        return s              
