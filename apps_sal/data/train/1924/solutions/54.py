class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        lenth = len(transactions)
        ans = set()
        for i in range(lenth):
            (name, time, price, city) = transactions[i].split(',')
            if int(price) > 1000:
                ans.add(transactions[i])
            for j in range(i, lenth):
                (n_name, n_time, n_price, n_city) = transactions[j].split(',')
                if name == n_name and n_city != city and (abs(int(n_time) - int(time)) <= 60):
                    ans.add(transactions[i])
                    ans.add(transactions[j])
        return ans
