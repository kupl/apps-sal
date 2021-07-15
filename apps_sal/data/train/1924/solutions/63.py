import collections
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        byName = collections.defaultdict(list)
        invalids = set()
        for transaction in transactions:
            name, t_min, amt, city = transaction.split(',')
            byName[name].append((int(t_min), int(amt), city, transaction))
            if int(amt) > 1000:
                invalids.add(transaction)
        for name in byName:
            trans = byName[name]
            for i in range(len(trans)):
                for j in range(i, len(trans)):
                    if abs(trans[i][0] - trans[j][0]) <= 60 and trans[i][2] != trans[j][2]: 
                        invalids.add(trans[i][3])
                        invalids.add(trans[j][3])
        return list(invalids)
