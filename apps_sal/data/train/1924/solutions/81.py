class Transaction:

    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city


class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [Transaction(*t.split(',')) for t in transactions]
        transactions.sort(key=lambda x: x.time)
        nameMap = collections.defaultdict(list)
        for (i, t) in enumerate(transactions):
            nameMap[t.name].append(i)
        invalid = []
        for (name, idxLst) in nameMap.items():
            left = 0
            right = 0
            for idx in idxLst:
                t = transactions[idx]
                if t.amount > 1000:
                    invalid.append(f'{t.name},{t.time},{t.amount},{t.city}')
                    continue
                while left < len(idxLst) and transactions[idxLst[left]].time < t.time - 60:
                    left += 1
                while right < len(idxLst) and transactions[idxLst[right]].time <= t.time + 60:
                    right += 1
                for i in range(left, right):
                    if t.city != transactions[idxLst[i]].city:
                        invalid.append(f'{t.name},{t.time},{t.amount},{t.city}')
                        break
        return invalid
