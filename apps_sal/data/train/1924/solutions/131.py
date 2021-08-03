class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = []
        n = len(transactions)
        rank = [True] * n
        name = []
        time = []
        amount = []
        city = []
        for t in transactions:
            num = t.split(',')
            name.append(num[0])
            time.append(num[1])
            amount.append(num[2])
            city.append(num[3])

        for i in range(n):
            if int(amount[i]) > 1000:
                rank[i] = False
            for j in range(i + 1, n):
                if name[i] == name[j] and abs(int(time[i]) - int(time[j])) <= 60 and city[i] != city[j]:
                    rank[i] = False
                    rank[j] = False
        for t in range(n):
            if not rank[t]:
                ans.append(transactions[t])

        return ans
