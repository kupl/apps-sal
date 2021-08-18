class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions_by_name = {}
        suspicious_transactions = set()
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            if name not in transactions_by_name:
                transactions_by_name[name] = [[name, time, amount, city]]
            else:
                transactions_by_name[name].append([name, time, amount, city])
        for key in transactions_by_name.keys():
            for transaction in transactions_by_name[key]:
                for other_transaction in transactions_by_name[key]:
                    if int(transaction[2]) >= 1000 and ','.join(transaction) not in suspicious_transactions:
                        suspicious_transactions.add(','.join(transaction))
                        continue
                    if transaction == other_transaction:
                        continue
                    time_diff = abs(int(transaction[1]) - int(other_transaction[1]))
                    print(time_diff)
                    if time_diff <= 60 and transaction[3] != other_transaction[3]:
                        suspicious_transactions.add(','.join(transaction))
        return list(suspicious_transactions)
