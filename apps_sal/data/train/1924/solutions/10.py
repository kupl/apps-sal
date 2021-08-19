class Solution:
    from heapq import heappush, heappop

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        memo = collections.defaultdict(list)
        invalid_tran = set()
        for i in range(len(transactions)):
            (name, time, amount, city) = (int(i) if i.isnumeric() else i for i in transactions[i].split(','))
            if amount > 1000:
                invalid_tran.add(transactions[i])
            if name in memo:
                for tran in memo[name]:
                    (_, prev_time, _, prev_city) = (int(i) if i.isnumeric() else i for i in tran.split(','))
                    if abs(time - prev_time) <= 60 and prev_city != city:
                        invalid_tran.add(tran)
                        invalid_tran.add(transactions[i])
            memo[name].append(transactions[i])
        return invalid_tran
