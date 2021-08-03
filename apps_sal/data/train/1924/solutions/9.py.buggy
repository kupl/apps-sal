class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        LIMIT_AMOUNT = 1000
        LIMIT_TIME = 60
        
        invalid_list = set()
        t_parsed = [x.split(\",\") for x in transactions]
        
        for t in t_parsed:
            t[1] = int(t[1])
            t[2] = int(t[2])
        
        for i in range(len(t_parsed)):
            exceeding = t_parsed[i][2] > LIMIT_AMOUNT
            if exceeding:
                invalid_list.add(i)
                
            for j in range(i+1, len(t_parsed)):
                if i != j and \\
                        abs(t_parsed[i][1]-t_parsed[j][1]) <= LIMIT_TIME and \\
                        t_parsed[i][0] == t_parsed[j][0] and \\
                        t_parsed[i][3] != t_parsed[j][3]:
                    invalid_list.add(i)
                    invalid_list.add(j)
                    
        return [transactions[x] for x in invalid_list]
            
