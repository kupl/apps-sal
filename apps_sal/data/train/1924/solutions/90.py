class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transMap = dict()  # name: [time, city, t]
        invalids = set()

        for t in transactions:
            name, time, amount, city = t.split(',')
            if int(amount) > 1000:
                invalids.add(t)
            if name in transMap:
                for stime, scity, st in transMap[name]:
                    if abs(int(time) - int(stime)) <= 60 and city != scity:
                        invalids.add(st)
                        invalids.add(t)
            else:
                transMap[name] = []
            transMap[name].append((time, city, t))
        return list(invalids)
