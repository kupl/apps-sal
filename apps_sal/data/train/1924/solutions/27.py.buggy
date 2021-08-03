class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        temp = []
        for transaction in transactions:
            name, time, amount, city = transaction.split(\",\")
            temp.append([name, int(time), int(amount), city, transaction])
        
        ans = set()
        for transaction1 in temp:
            if transaction1[2] > 1000:
                ans.add(transaction1[4])
            for transaction2 in temp:
                if transaction1[0] == transaction2[0] and abs(transaction1[1] - transaction2[1]) <= 60 and transaction1[3] != transaction2[3]:
                    ans.add(transaction2[4])
        return list(ans)
                
                     
           
        
