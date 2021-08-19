class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        res = set()
        names = defaultdict(list)
        time, amt, city = [], [], []
        for i, ele in enumerate(transactions):
            s = ele.split(',')
            names[s[0]] += [(int(s[1]), int(s[2]), s[3], s[0])]

        for k, v in list(names.items()):

            for i, ele in enumerate(v):
                b, c, d, a = ele
                for j in range(0, len(v)):
                    if i != j:
                        f, g, h, e = v[j]
                        if (abs(b - f) <= 60) and (a == e) and (d != h):
                            res.add(a + ',' + str(b) + ',' + str(c) + ',' + d)
                            res.add(e + ',' + str(f) + ',' + str(g) + ',' + h)
                    if c > 1000:
                        res.add(a + ',' + str(b) + ',' + str(c) + ',' + d)

                # if i>=1:
                #     e,f,g,h = v[i-1].split(',')
                #     if (abs(int(b)-int(f)) <= 60) and (a == e) and (d != h):
                #         res.add(a+','+str(b)+','+str(c)+','+d)
                #         res.add(e+','+str(f)+','+str(g)+','+h)
                # if int(c) > 1000:
                #     res.add(a+','+str(b)+','+str(c)+','+d)

        return res
