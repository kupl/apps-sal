class Transaction:
    
    def __init__(self, s):
        params = s.split(',')
        
        self.name, self.time, self.amount, self.city = params[0], int(params[1]), int(params[2]), params[3]
        
    def __str__(self):
        return ','.join([self.name, str(self.time), str(self.amount), self.city])
    
    

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        transactions = [Transaction(t) for t in transactions]
        
        transactions.sort(key = lambda t: t.time)
        
        #map name to transaction idx
        trans_idxs = defaultdict(list)
        
        for i, t in enumerate(transactions):
            trans_idxs[t.name].append(i)
            
        invalid = []
        
        for name, idxs in list(trans_idxs.items()):
            left = right = 0
            
            for trans_idx in idxs:
                t = transactions[trans_idx]
                if t.amount > 1000:
                    invalid.append(str(t))
                    continue
                
                while left <= len(idxs) - 2 and transactions[idxs[left]].time < t.time - 60:
                    left += 1
                    
                right = left
                while right <= len(idxs) - 2 and transactions[idxs[right+1]].time < t.time + 60:
                    right += 1
                
                for j in range(left, right+1):
                    if transactions[idxs[j]].city != t.city:
                        invalid.append(str(t))
                        break
                        
        return invalid
                    
                

