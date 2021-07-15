class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # { name -> {time -> amount city i} 
        invalidIdxList = set()
        transDict = {}
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            if int(amount) > 1000:
                invalidIdxList.add(i)
            j = i + 1
            while j < len(transactions):
                otherName, otherTime, otherAmount, otherCity = transactions[j].split(',')
                if name == otherName and abs(int(time) - int(otherTime)) <= 60 and city != otherCity:
                    invalidIdxList.add(i)
                    invalidIdxList.add(j)
                j = j + 1
        res = []
        for idx in invalidIdxList:
            res.append(transactions[idx])
        return res
              

                    
                    
                    
                    
            
                
            
        

