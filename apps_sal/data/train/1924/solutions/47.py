class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalidTct = []
        for i in range(len(transactions)):
            name1, time1, amount1, location1 = transactions[i].split(',')
            if int(amount1) > 1000:
                invalidTct.append(transactions[i])
            for j in range(i + 1, len(transactions)):
                name2, time2, amount2, location2 = transactions[j].split(',')
                if name1 == name2 and abs(int(time1) - int(time2)) <= 60 and location1 != location2:
                    invalidTct.append(transactions[i])
                    invalidTct.append(transactions[j])
        return list(set(invalidTct))
