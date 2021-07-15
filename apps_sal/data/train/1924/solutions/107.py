from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # occurs within 60 mins of another transaction,
        # does the previous transaction need to be valid? -> No
        invalid = set()
        records = defaultdict(list)
        for transaction in transactions:
            name, time, value, city = transaction.split(\",\")
            if int(value) > 1000:
                invalid.add(transaction)
            if name in records:
                for record in records[name]:
                    last_name, last_time, last_value, last_city = record.split(\",\")
                    if abs(int(time) - int(last_time)) <= 60 and city != last_city:
                        invalid.add(record)
                        invalid.add(transaction)
            records[name].append(transaction)
        return invalid
            
