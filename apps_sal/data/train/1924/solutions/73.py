class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        M = collections.defaultdict(dict)

        ans = set()
        for t in transactions:
            name, time, amount, city = t.split(',')
            if int(amount) > 1000:
                ans.add(t)

            Flag = False
            if name in M:
                for k, v in list(M[name].items()):
                    if abs(int(time) - k) <= 60 and v.split(',')[-1] != city:
                        ans.add(v)
                        Flag = True
            M[name][int(time)] = t
            if Flag:
                ans.add(t)

        return list(ans)
