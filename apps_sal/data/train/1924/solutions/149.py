import collections


class Solution(object):

    def invalidTransactions(self, transactions):
        if not transactions:
            return []
        memo = {}
        invalid_tran = set()
        for (i, transaction) in enumerate(transactions):
            (name, time, amount, city) = (int(i) if i.isnumeric() else i for i in transaction.split(','))
            if amount > 1000:
                invalid_tran.add(transaction)
            if name in memo:
                for tran in memo[name]:
                    (_, prev_time, _, prev_city) = (int(i) if i.isnumeric() else i for i in tran.split(','))
                    if abs(time - prev_time) <= 60 and prev_city != city:
                        invalid_tran.add(tran)
                        invalid_tran.add(transaction)
            if name not in memo:
                memo[name] = []
            memo[name].append(transaction)
        return invalid_tran
