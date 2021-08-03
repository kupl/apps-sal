class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions_dict = defaultdict(list)
        invalid = []
        for i in range(len(transactions)):
            details = transactions[i].split(\",\")
            if int(details[2]) > 1000:
                invalid.append(transactions[i])
            
            for j in range(i+1, len(transactions)):
                name,time, amount,city = transactions[j].split(\",\")
                if abs(int(details[1]) - int(time)) <=60 and details[0] == name :
                    if (details[3] != city):
                        invalid.append(transactions[i])
                        invalid.append(transactions[j])
                
        return list(set(invalid))
        
