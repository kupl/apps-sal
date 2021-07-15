class Solution:
    def invalidTransactions(self, ts: List[str]) -> List[str]:
        nts = [t.split(',') for t in ts]
        nts = sorted([[a, int(b), int(c), d] for a, b, c, d in nts])
        res = set()
        for a in nts:
            if a[2] > 1000: res.add(','.join(map(str,a)))
        for i in range(len(nts)):
            for j in range(i + 1, len(nts)):
                a, b = nts[i], nts[j]
                if a[0] != b[0] or abs(a[1] - b[1]) > 60: break
                if a[3] != b[3]: 
                    res.add(','.join(map(str,a)))
                    res.add(','.join(map(str,b)))
        return list(res)
