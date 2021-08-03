class Solution:
    # > 1000
    # same name, different city, <= 60 min
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
#         loop through transactions 
#             if amount is greater >= 1000 add it to invalid set
#             have another loop, check every other transactions for invalid time
         
        # { invalidtransaction}
        # {
        #     alice: [\"transaction\",\"transaction\"]
        #     bob: [\"transaction\"]
        # }
        
        userTransactions = collections.defaultdict(list)
        invalidTransactions = set()
        
        for transaction in transactions:
            [name,time,amount,city] = transaction.split(\",\")
            
            if int(amount) > 1000: invalidTransactions.add(transaction)
            userTransactions[name].append(transaction)
            
        for name in userTransactions:
            userTrans = userTransactions[name]
            
            for i in range(len(userTrans)-1):
                for j in range(i+1,len(userTrans)):
                    [_,time,_,city] = userTrans[i].split(\",\")
                    [_,time2,_,city2] = userTrans[j].split(\",\")
                    
                    if abs(int(time)-int(time2)) <= 60 and city != city2:
                        invalidTransactions.add(userTrans[i])
                        invalidTransactions.add(userTrans[j])
                    
        return list(invalidTransactions)
            
                
        
        
        
