class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        for i in range(len(transactions)):
            added = False
            for j in range(i + 1, len(transactions)):
                a = transactions[i].split(',')
                b = transactions[j].split(',')
                if a[0] == b[0] and a[-1] != b[-1] and abs(int(a[1]) - int(b[1])) <= 60:
                    res.append(','.join(a))
                    res.append(','.join(b))
                    added = True
            if not added:
                if int(transactions[i].split(',')[2]) > 1000:
                    res.append(transactions[i])

        return list(set(res))
