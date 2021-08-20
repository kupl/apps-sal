class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        for (i, t) in enumerate(transactions):
            (name, time, amount, city) = t.split(',')
            if int(amount) > 1000:
                invalid.add(i)
                continue
            for j in range(len(transactions)):
                if i == j:
                    continue
                (jname, jtime, jamount, jcity) = transactions[j].split(',')
                if jname == name and jcity != city and (abs(int(jtime) - int(time)) <= 60):
                    invalid.add(i)
                    invalid.add(j)
        return [transactions[i] for i in invalid]
