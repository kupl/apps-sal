class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # first check : if amount > 1000 invalid
        # second check : else:
        #       if name equals with another transaction : if time_this - time_that <60 and city not equal both invalid
        #                                                 if time_this - time_that <60 and city equal both valid
        
        tr = {}
        invalids = set()
        
        for t in transactions:
            tl = t.split(',')
            
            if tl[0] not in tr:                 
                tr[tl[0]] = [t]
                if int(tl[2]) > 1000:  # amount > 1000
                    invalids.add(t)                
                    
            else:   # name equal                
                if int(tl[2]) > 1000:  # amount > 1000
                    invalids.add(t)                   
                tmp = tr[tl[0]]  # amount < 1000                 
                for temp in tmp:                        
                    tempo = temp.split(',')                        
                    if tempo[3] != tl[3]: # city not equal
                        if abs(int(tempo[1])- int(tl[1])) <= 60:  # less than 60 min
                            invalids.add(t) 
                            invalids.add(temp)
                                  
                tr[tl[0]].append(t)               
        return invalids

