class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        mapping = {}
        result = []
        for trans in transactions:
            info = trans.split(\",\")  
            if int(info[2]) > 1000:
                result.append(trans)
            if info[0] not in mapping:
                mapping[info[0]] = [info[1:]]
            else:
                
                for mapTransaction in mapping[info[0]]:
                    if (mapTransaction[2] != info[3]) and (abs(int(mapTransaction[0]) - int(info[1])) <= 60):
                        trans1 = ','.join([info[0]] + mapTransaction[:])
                        if trans1 not in result:
                            result.append(trans1)
                        if trans not in result:
                            result.append(trans)        
                mapping[info[0]].append(info[1:])
            
        return result
            

                

        
                    
            
                
        
