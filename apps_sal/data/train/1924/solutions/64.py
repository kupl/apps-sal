class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactionDict = {}
        invalid = []
        for i in transactions:
            transactionData = i.split(',')
            name, time, amount, city = transactionData[0], transactionData[1], transactionData[2], transactionData[3]
            if name in transactionDict.keys():
                transactionVal = transactionDict[name]
            else:
                transactionVal = []
            transactionVal.append([time, amount, city])
            transactionDict[name] = transactionVal
        for i in transactionDict.keys():
            for v in transactionDict[i]:
                # test if transaction over 1000
                if int(v[1]) > 1000:
                    if '{},{},{},{}'.format(i, v[0], v[1], v[2]) not in invalid:
                        invalid.append('{},{},{},{}'.format(i, v[0], v[1], v[2]))
                # test if any other transaction time within 60 in a different city
                for listd in transactionDict[i]:
                    if listd != v:
                        if abs(int(v[0]) - int(listd[0])) <= 60 and v[2] != listd[2]:
                            if '{},{},{},{}'.format(i, v[0], v[1], v[2]) not in invalid:
                                invalid.append('{},{},{},{}'.format(i, v[0], v[1], v[2]))
        return invalid
