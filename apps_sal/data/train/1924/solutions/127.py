class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        t = transactions.copy()
        t.sort()
        invalid = set()
        name = \"\"
        times = {}
        for transaction in t:
            vals = transaction.split(',')
            if int(vals[2]) > 1000:
                invalid.add(transaction)
            if vals[0] != name:
                name = vals[0]
                times[name] = list()
            else:
                for seen in times[name]:
                    vs = seen.split(',')
                    if vs[3] != vals[3] and abs(int(vs[1]) - int(vals[1])) <= 60:
                        invalid.add(seen)
                        invalid.add(transaction)
            times[name].append(transaction)
        
        return list(invalid)
