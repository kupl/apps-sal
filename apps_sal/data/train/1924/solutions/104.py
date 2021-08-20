class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        for (i, t1) in enumerate(transactions):
            item = t1.split(',')
            val = int(item[2])
            minute = int(item[1])
            name = item[0]
            city = item[-1]
            if val > 1000:
                res.append(t1)
                continue
            for (j, t2) in enumerate(transactions):
                if i != j:
                    item = t2.split(',')
                    val2 = int(item[2])
                    minute2 = int(item[1])
                    name2 = item[0]
                    city2 = item[-1]
                    if abs(minute2 - minute) <= 60 and name2 == name and (city2 != city):
                        res.append(t1)
                        break
        return res
