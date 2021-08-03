class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = []
        num = len(transactions)
        added = set()
        for i in range(num):
            name1, time1, num1, city1 = transactions[i].split(',')
            if int(num1) > 1000 and i not in added:
                ans.append(transactions[i])
                added.add(i)
            for j in range(i + 1, num):
                name2, time2, num2, city2 = transactions[j].split(',')
                if (name1 == name2
                    and abs(int(time2) - int(time1)) <= 60
                        and city2 != city1):
                    if i not in added:
                        ans.append(transactions[i])
                        added.add(i)
                    if j not in added:
                        ans.append(transactions[j])
                        added.add(j)
        return ans
