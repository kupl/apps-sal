class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        splits = [t.split(',') for t in transactions]
        lists = {}
        res = set()
        for (time, p, v, loc, t) in sorted([[int(sp[1]), sp[0], int(sp[2]), sp[3], t] for (sp, t) in zip(splits, transactions)]):
            if v > 1000:
                res.add(t)
            tk = time % 61
            if p not in lists:
                lists[p] = [None] * 61
            lst = lists[p]
            for i in range(61):
                if lst[i] and abs(lst[i][0] - time) <= 60 and (lst[i][1] != loc):
                    res.add(t)
                    res.add(lists[p][i][2])
            lst[tk] = [time, loc, t]
        return res
