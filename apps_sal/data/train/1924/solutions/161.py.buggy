class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        trans = [i.split(\",\") for i in transactions]
        for i in range(len(transactions)):
            if int(trans[i][2]) > 1000:
                invalid.add(transactions[i])
            for j in range (i, len(transactions)):
                if trans[i][0] == trans[j][0] and trans[i][3] != trans[j][3] and abs(int(trans[i][1]) - int(trans[j][1])) <= 60:
                    invalid.add(transactions[i])
                    invalid.add(transactions[j])
        return list(invalid)
