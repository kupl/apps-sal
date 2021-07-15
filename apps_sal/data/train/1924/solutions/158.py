class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        records = []
        for transaction in transactions:
            name, time, amount, city = transaction.split(\",\")
            records.append((name, int(time), int(amount), city, transaction))
        answer = set()
        for record in records:
            if record[2] > 1000:
                answer.add(record[4])
                continue
            for other in records:
                if record[0] == other[0] and record[3] != other[3] and abs(record[1] - other[1]) <= 60:
                    answer.add(record[4])
                    answer.add(other[4])
        return list(answer)
            
