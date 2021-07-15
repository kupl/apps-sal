class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        invalid = set()
        past_tran = {}
        for transaction in transactions:
            tran = transaction.split(',')
            tran[2]=float(tran[2])
            tran[1]=float(tran[1])
            if tran[2]>1000:
                invalid.add(transaction)
            if tran[0] in past_tran:
                for other_transaction in past_tran[tran[0]]:
                    other_tran = other_transaction.split(',')
                    other_tran[1]=float(other_tran[1])
                    if other_tran[3]!=tran[3] and abs(tran[1]-other_tran[1])<=60:
                        invalid.add(transaction)   
                        invalid.add(other_transaction)
                past_tran[tran[0]].append(transaction)
                                                    
            else:
                past_tran[tran[0]]=[transaction]
        return list(invalid)

