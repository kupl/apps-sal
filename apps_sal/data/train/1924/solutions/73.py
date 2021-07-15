class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        M = collections.defaultdict(dict)
        
        ans = set()  # avoid duplicate
        for t in transactions:
            name, time, amount, city = t.split(',')
            if int(amount) > 1000:              # invalid condition 1
                ans.add(t)

            Flag = False
            if name in M:                       # have transaction under the name
                for k,v in list(M[name].items()):     # iterate all (time, transaction) pairs under this name
                    if abs(int(time)-k) <= 60 and v.split(',')[-1] != city:  # invalid condition 2
                        ans.add(v)
                        Flag = True             # add current transaction
            M[name][int(time)] = t              # add transaction to HashMap
            if Flag:
                ans.add(t)
        
        return list(ans)

