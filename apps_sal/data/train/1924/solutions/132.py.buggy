class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        \"\"\"
        There are two ways for transaction to be invalid.
        1. Exceeds 1000. -> iterate and put each into a bin
        2. Same name in a different city within a 60 second window
        \"\"\"
        invalid_transactions = set()
        trans_by_name = {}
        # For the trans_by_name, add by name, then by city
        # As a new transaction arrives, check to see if the difference 
        #   between it and the transactions under a different name which 
        #   do not have the same city name. If not, add it to the table.
        #   If so, also add it to the invalid_transactions list
        for trans in transactions:
            tname, tmin, tamt, tcity = trans.split(',')
            if int(tamt) > 1000:
                invalid_transactions.add(trans)
            if tname in trans_by_name:
                for city, time, amt in trans_by_name[tname]:
                    if tcity != city and abs(int(tmin) - int(time)) <= 60:
                        print(f'{tname} {time} {city} {amt}')
                        invalid_transactions.add(trans)
                        invalid_transactions.add(f'{tname},{time},{amt},{city}')
            if tname not in trans_by_name:
                trans_by_name[tname] = set()
            trans_by_name[tname].add((tcity, tmin, tamt))
        return invalid_transactions
        
