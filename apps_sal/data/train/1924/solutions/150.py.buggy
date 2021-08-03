class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        transactionsByName = {}
        invalidTransactions = set()
        for t in transactions:
            name, time, amount, city = t.split(\",\")
            if int(amount) > 1000:
                
                invalidTransactions.add(t)
                
            item = {
                \"name\": name,
                \"time\": time,
                \"amount\": amount,
                \"city\": city,
            }
            
            if name not in transactionsByName:
                transactionsByName[name] = [item]
            else:
                transactionsByName[name].append(item)
        
        for key, values in transactionsByName.items():
            # values.sort(key = lambda v: v[\"time\"]) 
            for i in range(len(values)):
                for k in range(len(values)):
                    if values[i][\"city\"] != values[k][\"city\"] and abs(int(values[i][\"time\"]) - int(values[k][\"time\"])) <=60:
                        invalidTransactions.add(\",\".join(values[i].values()))
                        invalidTransactions.add(\",\".join(values[k].values()))

        return list(invalidTransactions)
        # same name -> go through list 
        # sort by time
        # if each one is next to other, put first into list if last, put that to list too
        
