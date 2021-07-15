class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        watch_set = set([])
        prev_user = {}
        # Loop once through transactions
        for idx, trans in enumerate(transactions):
            name, time, amt, city = trans.split(\",\")
            time = int(time)
            amt = int(amt)
            if amt > 1000:
                watch_set.add(idx)
            if name in prev_user:
                for p_idx, p_time, p_city in prev_user[name]:
                    if abs(p_time - time) <= 60 and p_city != city:
                        watch_set.add(idx)
                        watch_set.add(p_idx)
                prev_user[name].append((idx, time, city))
            else:
                prev_user[name] = [(idx, time, city)]
        return [transactions[idx] for idx in watch_set]
