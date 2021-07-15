class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalids = set()
        
        
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(',')
            if int(amount) > 1000:
                invalids.add(transactions[i])
            j = i +1
            while j < len(transactions):
                nameJ, timeJ, amountJ, cityJ = transactions[j].split(',')
                if nameJ == name and abs(int(timeJ) - int(time)) <= 60 and city != cityJ:
                    invalids.add(transactions[i])
                    invalids.add(transactions[j])
                j+=1
        return list(invalids)
            
                
        print (invalids)
        \"\"\"
        Hashtable => NO
        
        Two Pointer yes
        
        
        
        \"\"\"
        
