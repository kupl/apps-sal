class Solution:

    def invalidTransactions(self, transactions):
        transactions.sort()
        n = len(transactions)
        result = set()
        for i in range(n):
            (i_name, i_time, i_amount, i_city) = transactions[i].split(',')
            if int(i_amount) > 1000:
                result.add(transactions[i])
            for j in range(i + 1, n):
                (j_name, j_time, j_amount, j_city) = transactions[j].split(',')
                if j_name != i_name:
                    break
                if i_city != j_city and abs(int(i_time) - int(j_time)) <= 60:
                    result.add(transactions[i])
                    result.add(transactions[j])
        return list(result)
