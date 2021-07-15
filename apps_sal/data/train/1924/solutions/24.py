class Solution(object):
    def invalidTransactions(self, transactions):
        NAME, TIME, AMOUNT, CITY = list(range(4))
        
        txrows = []
        for row in transactions:
            name, time, amount, city = row.split(',')
            time = int(time)
            amount = int(amount)
            txrows.append((name, time, amount, city))
        
        ans = []
        for i, tx1 in enumerate(txrows):
            if tx1[AMOUNT] >= 1000:
                ans.append(transactions[i])
                continue
            for j, tx2 in enumerate(txrows):
                if (i != j and abs(tx1[TIME] - tx2[TIME]) <= 60 and
                        tx1[NAME] == tx2[NAME] and tx1[CITY] != tx2[CITY]):
                    ans.append(transactions[i])
                    break
        
        return ans

