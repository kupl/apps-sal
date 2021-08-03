class Solution:
    # 0) split each element of transactions on comma
    # 1) iterate through transactions and if amount > 1000 add to ans array and transactions.pop(i)
    # 2) create dict {name:[...(time, city)...]}    # sort by time
    # 3) iterate through transactions and if within 60 minutes and diff city then add to ans array
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # 0)
        transactions = [string.split(',') for string in transactions]

        # 1)
        ans, length = set(), len(transactions)
        for i in range(length):
            if int(transactions[i][2]) > 1000:
                ans.add(','.join(transactions[i]))

        # 2)
        dct = {}
        for i in range(length):
            name, time, city = transactions[i][0], transactions[i][1], transactions[i][-1]
            if name in dct:
                dct[name].append((time, city))
                dct[name].sort()
            else:
                dct[name] = [(time, city)]

        # 3)
        for name, time, amt, city in transactions:
            for tme, cty in dct[name]:
                if abs(int(time) - int(tme)) <= 60 and city != cty:
                    ans.add(','.join([name, time, amt, city]))
        return list(ans)
