from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions.sort(key=lambda t: int(t.split(',')[1]))
        recent = defaultdict(lambda: [])
        result = set()
        for transaction in transactions:
            name, time, amount, city = self.parse(transaction)
            if amount > 1000:
                result |= {transaction}
            if name in recent:
                for recent_transaction in recent[name]:
                    _, recent_time, _, recent_city = self.parse(recent_transaction)
                    if time - recent_time <= 60 and recent_city != city:
                        result |= {recent_transaction, transaction}
            recent[name] += [transaction]
        return result

    def parse(self, transaction):
        name, time, amount, city = transaction.split(',')
        return name, int(time), int(amount), city
