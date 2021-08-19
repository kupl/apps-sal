class Solution:

    def invalidTransactions(self, transactions):
        transactions = [t.split(',') for t in transactions]
        t = defaultdict(list)
        res = set()
        for x in transactions:
            t[x[0]].append([int(x[1]), int(x[2]), x[3]])
        for name in t:
            t[name].sort(key=lambda x: x[0])
            for i in range(len(t[name])):
                (time1, amount1, city1) = t[name][i]
                if amount1 > 1000:
                    res.add(','.join([name, str(time1), str(amount1), city1]))
                for j in range(i + 1, len(t[name])):
                    (time2, amount2, city2) = t[name][j]
                    if amount2 > 1000:
                        res.add(','.join([name, str(time2), str(amount2), city2]))
                    if city1 == city2:
                        continue
                    if time2 - time1 <= 60:
                        res.add(','.join([name, str(time1), str(amount1), city1]))
                        res.add(','.join([name, str(time2), str(amount2), city2]))
                    else:
                        break
        return res
