class Solution:

    def invalidTransactions(self, transactions):
        if not transactions:
            return []
        n = len(transactions)
        splits = [trans.split(',') for trans in transactions]
        valid = [True] * n

        for i in range(n):
            if int(splits[i][2]) > 1000:
                valid[i] = False

        for i in range(n):
            for j in range(i + 1, n):
                if valid[i] or valid[j]:
                    name1, time1, city1 = splits[i][0], int(splits[i][1]), splits[i][3]
                    name2, time2, city2 = splits[j][0], int(splits[j][1]), splits[j][3]
                    if name1 == name2 and city1 != city2 and abs(time1 - time2) <= 60:
                        valid[i], valid[j] = False, False

        return [transactions[i] for i in range(n) if not valid[i]]

        '''
        sort the transaction list as per the time
        
        a dictionary where key is the name of the person and the the value is a dictionary where the key is the city and the value is time and amount        
        
        
        
        iterate over the transactions:
            if the amount is greater than 1000:
                add it to the list
            
            if that same person has done a transaction before
                are the cities different:
                    get the time of the latest transaction
                    if difference is <60:
                        add the latest transaction as well as this transaction
                        update the latest transaction with this transaction info
                        continue
                        
                 
        '''
