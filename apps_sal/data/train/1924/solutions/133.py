class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        personDict = dict()
        outSet = set()
        for transaction in transactions:
            (name, time, amount, city) = transaction.split(',')
            if int(amount) > 1000:
                outSet.add(transaction)
            if name in personDict:
                cityDict = personDict[name]
                cityDict[city].append((time, amount))
                for key in cityDict:
                    if key != city:
                        for pair in cityDict[key]:
                            (prevTime, prevAmount) = pair
                            timeDiff = abs(int(time) - int(prevTime))
                            if timeDiff <= 60:
                                outSet.add(transaction)
                                outSet.add(','.join([name, prevTime, prevAmount, key]))
            else:
                personDict[name] = defaultdict(list)
                personDict[name][city].append((time, amount))
        return outSet
        '\n        sort the transaction list as per the time\n        \n        a dictionary where key is the name of the person and the the value is a dictionary where the key is the city and the value is time and amount        \n        \n        \n        \n        iterate over the transactions:\n            if the amount is greater than 1000:\n                add it to the list\n            \n            if that same person has done a transaction before\n                are the cities different:\n                    get the time of the latest transaction\n                    if difference is <60:\n                        add the latest transaction as well as this transaction\n                        update the latest transaction with this transaction info\n                        continue\n                        \n                 \n        '
