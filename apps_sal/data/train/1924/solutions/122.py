class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [string.split(',') for string in transactions]

        ans, length = set(), len(transactions)
        for i in range(length):
            if int(transactions[i][2]) > 1000:
                ans.add(','.join(transactions[i]))

        dct = {}
        for i in range(length):
            name, time, city = transactions[i][0], transactions[i][1], transactions[i][-1]
            if name in dct:
                dct[name].append((time, city))
                dct[name].sort()
            else:
                dct[name] = [(time, city)]

        for name, time, amt, city in transactions:
            for tme, cty in dct[name]:
                if abs(int(time) - int(tme)) <= 60 and city != cty:
                    ans.add(','.join([name, time, amt, city]))
        return list(ans)
