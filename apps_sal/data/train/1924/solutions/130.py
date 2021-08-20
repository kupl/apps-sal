class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tf_arr = [True for _ in range(len(transactions))]
        new_transactions = []
        for x in transactions:
            x = x.split(',')
            x[1] = int(x[1])
            x[2] = int(x[2])
            new_transactions.append(x)

        def check(transaction, i, arr):
            if transaction[2] > 1000:
                tf_arr[i] = False
            for (j, e) in enumerate(arr[i + 1:]):
                if transaction[0] == e[0] and transaction[3] != e[3] and (abs(transaction[1] - e[1]) <= 60):
                    tf_arr[i] = False
                    tf_arr[i + j + 1] = False
        for (i, t) in enumerate(new_transactions):
            check(t, i, new_transactions)
        output = []
        for (i, truth) in enumerate(tf_arr):
            if not truth:
                output.append(transactions[i])
        return output
