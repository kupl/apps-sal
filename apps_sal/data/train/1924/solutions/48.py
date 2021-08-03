class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        invalidSet = set()
        for i, transaction in enumerate(transactions):
            name1, time1, amount1, city1 = transaction.split(',')
            if int(amount1) > 1000:
                invalidSet.add(transaction)
            for j in range(i + 1, len(transactions)):
                name2, time2, amount2, city2 = transactions[j].split(',')
                if name1 == name2 and abs(int(time2) - int(time1)) <= 60 and city1 != city2:
                    invalidSet.add(transactions[j])
                    invalidSet.add(transaction)

        return invalidSet
