class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions or len(transactions) == 0:
            return []
        d = collections.defaultdict(dict)
        res = set()
        for t in transactions:
            (name, time, amount, city) = t.split(',')
            if int(amount) > 1000:
                res.add(t)
            flag = False
            if name in d:
                for (_time, _t) in d[name].items():
                    if abs(_time - int(time)) <= 60 and city != _t.split(',')[-1]:
                        flag = True
                        res.add(_t)
            if flag:
                res.add(t)
            d[name][int(time)] = t
        return list(res)
