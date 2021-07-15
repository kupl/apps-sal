class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        def parseTransaction(t):
            vals = t.split(',')
            return vals[0], int(vals[1]), int(vals[2]), vals[3]

        
        invalid = set()
        names = {}
        for t in transactions:
            name, time, amt, city = parseTransaction(t)
            if amt > 1000:
                invalid.add(t)
            
            if name in names:
                for (other_t, other_time, other_city) in names[name]:
                    if other_city != city and abs(other_time - time) <= 60:
                        invalid.add(other_t)
                        invalid.add(t)
            else:
                names[name] = []

            names[name].append((t, time, city))
        
        return list(invalid)

