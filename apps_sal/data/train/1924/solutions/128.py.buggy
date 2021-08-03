class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        def reunite(temp):
            return temp[0] + \",\" + str(temp[1]) + \",\" + str(temp[2]) + \",\" + temp[3]
        new_transactions = []
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(\",\")
            new_transactions.append([name,int(time),int(amount),city])
            
        new_transactions.sort(key = lambda x: x[1])
        result = []
        for i in range(len(new_transactions)):
            if int(new_transactions[i][2]) > 1000:
                result.append(reunite(new_transactions[i]))
            
            for j in range(i,len(new_transactions)):
                if int(new_transactions[j][1]) - int(new_transactions[i][1]) <= 60 and new_transactions[j][3] != new_transactions[i][3] and new_transactions[j][0] == new_transactions[i][0]:
                    result.append(reunite(new_transactions[j]))
                    result.append(reunite(new_transactions[i]))
                elif int(new_transactions[j][1]) - int(new_transactions[i][1]) > 60:
                    break
        result.sort()
        new_result = [result[0]]
        for i in range(len(result)-1):
            if result[i] != result[i+1]:
                new_result.append(result[i+1])
                #print(new_result)
                
                
        return new_result
                
            
        
