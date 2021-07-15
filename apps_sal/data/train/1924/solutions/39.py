class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        
        for i in range(len(transactions)):
            action = transactions[i].split(',')
            person = action[0]
            time = action[1]
            amt = action[2]
            city = action[3]
            if int(amt) > 1000:
                res.append(transactions[i])
                
            for j in range(i+1, len(transactions)):
                act2 = transactions[j].split(',')
                if act2[0] == person and abs(int(act2[1]) - int(time)) <= 60 and city != act2[3]:
                    res.extend([transactions[i], transactions[j]])
        return list(set(res))
