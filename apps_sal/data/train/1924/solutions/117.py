class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        # transactions = sorted(transactions)
        # print(transactions)
        res = set()
        names = defaultdict(list)
        time, amt, city = [], [], []
        for i, ele in enumerate(transactions):
            s = ele.split(',')
            names[s[0]] += [(int(s[1]), int(s[2]), s[3], s[0])]
        for k, v in list(names.items()):
            v = sorted(v)
            for i, ele in enumerate(v):
                b, c, d, a = ele
                for j, ele1 in enumerate(v):
                    if i != j:
                        f, g, h, e = ele1
                        if (abs(b - f) <= 60) and (a == e) and (d != h):
                            res.add(a + ',' + str(b) + ',' + str(c) + ',' + d)
                            res.add(e + ',' + str(f) + ',' + str(g) + ',' + h)
                if c > 1000:
                    res.add(a + ',' + str(b) + ',' + str(c) + ',' + d)

                # if i>=1:
                #     f,g,h,e = v[i-1]
                #     if (abs(b-f) <= 60) and (a == e) and (d != h):
                #         res.add(a+','+str(b)+','+str(c)+','+d)
                #         res.add(e+','+str(f)+','+str(g)+','+h)
                # if c > 1000:
                #     res.add(a+','+str(b)+','+str(c)+','+d)

        return res
