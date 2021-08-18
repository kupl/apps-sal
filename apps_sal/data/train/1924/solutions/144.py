class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        dic = defaultdict(list)
        invalid = set()
        for i in range(len(transactions)):
            name, time, amount, city = (int(i) if i.isnumeric() else i for i in transactions[i].split(','))
            if amount > 1000:
                invalid.add(transactions[i])
            if name in dic:
                for tran in dic[name]:
                    _, prev_time, _, prev_city = (int(i) if i.isnumeric() else i for i in tran.split(','))
                    if prev_city != city and abs(prev_time - time) <= 60:
                        invalid.add(tran)
                        invalid.add(transactions[i])
            dic[name].append(transactions[i])
        return list(invalid)
