class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = sorted(transactions, key=lambda transaction: int(transaction.split(\",\")[1]))
        # print(transactions)
        record = {}
        invalid = []
        for transaction  in transactions:
            parse = transaction.split(',')
            if int(parse[2]) > 1000:
                invalid.append(transaction)
                
                
            
            if parse[0] in record:
                for prev in record[parse[0]]:
                    time = int(prev.split(\",\")[1])
                    loc = prev.split(\",\")[3]
                    if int(parse[1]) <= time + 60 and parse[3] != loc:

                        if prev not in invalid:
                            invalid.append(prev)
                        if transaction not in invalid:
                            invalid.append(transaction)

#                 time = record[parse[0]][\"time\"]
#                 loc = record[parse[0]][\"loc\"]
                
#                     
                    
#                 record[parse[0]][\"time\"] = int(parse[1])
#                 record[parse[0]][\"loc\"] = parse[3]
                record[parse[0]].append(transaction)

            
            else:
                record[parse[0]] = [transaction]
        
        return invalid
