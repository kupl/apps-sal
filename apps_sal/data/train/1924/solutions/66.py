class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        name = []
        time = []
        amount = []
        city = []
        for t in transactions:
            n,t,a,c = t.split(\",\")
            name.append(n)
            time.append(int(t))
            amount.append(int(a))
            city.append(c)
        
        ans = set()
        N = len(transactions)
        for i in range(N):
            if amount[i] > 1000:
                ans.add(transactions[i])
            for j in range(N):
                if i == j: continue
                if name[i] == name[j] and abs(time[i]-time[j]) <= 60 and city[i] != city[j]:
                    ans.add(transactions[j])
        return ans
