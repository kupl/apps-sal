class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        res = set()
        n = len(transactions)
        for i in range(n):
            (n1, t1, a1, d1) = transactions[i].split(',')
            if int(a1) > 1000:
                res.add(transactions[i])
            for j in range(i + 1, n):
                (n0, t0, a0, d0) = transactions[j].split(',')
                if n0 == n1 and d1 != d0 and (abs(int(t1) - int(t0)) <= 60):
                    res.add(transactions[i])
                    res.add(transactions[j])
        ans = []
        for t in res:
            ans.append(t)
        print(res, ans)
        return ans
