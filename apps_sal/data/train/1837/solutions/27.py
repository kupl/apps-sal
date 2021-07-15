class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = {}        
        header = []
        result = []
        for i,lst in enumerate(orders):   
            if lst[2] not in header:
                header.append(lst[2])
            tmp_lst = table.get(int(lst[1]),[])
            tmp_lst.append(lst[2]) 
            table[int(lst[1])] = tmp_lst    
            
        header.sort()      
        
        for k in table:
            tmp_lst = []
            tmp_lst.append(k)
            for pos in header:                         
                tmp_lst.append(table[k].count(pos))
            result.append(tmp_lst)
        result.sort()       
        header.insert(0,\"Table\")
        result.insert(0,header)
        
        for i,lst in enumerate(result):
            result[i] = list(map(str,lst))
    
        return result
