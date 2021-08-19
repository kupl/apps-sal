class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        personalTransactions = {}
        invalidTransactions = set()
        for i in transactions:
            (name, time, amount, city) = i.split(',')
            if int(amount) > 1000:
                invalidTransactions.add(i)
            if name not in personalTransactions.keys():
                personalTransactions[name] = [(int(time), city, amount)]
                continue
            else:
                personalTransactions[name].append((int(time), city, amount))
                for j in personalTransactions[name]:
                    if city == j[1]:
                        continue
                    elif abs(j[0] - int(time)) <= 60:
                        invalidTransactions.add(i)
                        invalidTransactions.add(name + ',' + str(j[0]) + ',' + j[2] + ',' + j[1])
        return list(invalidTransactions)
