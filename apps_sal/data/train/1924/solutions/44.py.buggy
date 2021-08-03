class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        t = [x.split(',') for x in transactions]
        t.sort(key = lambda x: int(x[1]))
        invalid = set()
        
        for r in range(len(t)):
            
            if int(t[r][2]) > 1000:
                
                invalid.add(\",\".join(t[r]))
                
            for c in range(r+1, len(t)):
                
                if (int(t[c][1]) - int(t[r][1])) <= 60 and t[c][3] != t[r][3] and t[c][0] == t[r][0]:
                    
                    invalid.add(\",\".join(t[r]))
                    invalid.add(\",\".join(t[c]))
                    
        return(invalid)
                
                
                
                
            
            
