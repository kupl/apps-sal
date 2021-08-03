class Transaction:
    def __init__(self, transaction):
        trans_details = transaction.split(\",\")
        self.name = trans_details[0]
        self.time = int(trans_details[1])
        self.amount = int(trans_details[2])
        self.city = trans_details[3]
        
    def findAnotherTrans(self, transactions):
        for transaction in transactions:
            curTransact = Transaction(transaction)
            if(curTransact.name==self.name and curTransact.city!=self.city and abs(curTransact.time - self.time)<=60):
                return True
        return False
    
    
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        final_ans = []
        for trans in transactions:
            curTransact = Transaction(trans)
            if(curTransact.amount>1000):
                final_ans.append(trans)
            else:
                if(curTransact.findAnotherTrans(transactions)):
                    final_ans.append(trans)
                
        return final_ans
    
            
            
