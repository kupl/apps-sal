class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        seen = {}
        for transaction in transactions:
            # print(transaction)
            # print(seen)
            name, time, amt, city = transaction.split(\",\")
            named_t = seen.get(name)
            if int(amt) > 1000:
                invalid.append(transaction)
                if named_t:
                    named_t.append(transaction)
                else:
                    named_t = [transaction]
                seen[name] = named_t
            if named_t:
                for ti in named_t:
                    n, t, a, c = ti.split(\",\")
                    if abs(int(time) - int(t)) <= 60 and c != city:
                        if transaction not in invalid:
                            invalid.append(transaction)
                        if ti not in invalid:
                            invalid.append(ti)
                named_t.append(transaction)
            else:
                named_t = [transaction]
            seen[name] = named_t
        return invalid
        
