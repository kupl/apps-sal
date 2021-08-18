from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        out_idx = set()
        q = []
        bkt_max = -inf

        for idx, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            time = int(time)
            amount = int(amount)

            if amount > 1000:
                out_idx.add(idx)

            bkt_max = max(bkt_max, time + 30)

            q.append((max(time - 30, 0), time + 30, name, city, idx))

        bkt = [None] * (bkt_max + 1)
        for time_lower_bound, time_upper_bound, name, city, idx in q:
            for i in range(time_lower_bound, time_upper_bound + 1):
                if bkt[i] is None:
                    bkt[i] = defaultdict(lambda: defaultdict(lambda: set()))
                bkt[i][name][city].add(idx)

        for b in bkt:
            if b is not None:
                for k, v in list(b.items()):
                    if len(v) > 1:
                        for v1 in list(v.values()):
                            out_idx.update(v1)

        out = []
        for idx in out_idx:
            out.append(transactions[idx])

        return out
