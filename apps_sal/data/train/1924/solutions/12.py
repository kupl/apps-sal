class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # convert each into object Transaction
        for i in range(len(transactions)):
            transact = transactions[i].split(',')
            transactions[i] = Transaction(transact[0], transact[1], transact[2], transact[3])

        invalid = set()
        transactions.sort(key=lambda t: t.time)

        for i, t in enumerate(transactions):
            if t.amount > 1000:
                invalid.add(self.toString(t))
            for j in range(i + 1, len(transactions)):
                s = transactions[j]
                if t.name == s.name and t.city != s.city and s.time - t.time <= 60:
                    invalid.add(self.toString(s))
                    invalid.add(self.toString(t))
        return invalid

    def toString(self, s):
        return ('%s,%d,%d,%s' % (s.name, s.time, s.amount, s.city))
