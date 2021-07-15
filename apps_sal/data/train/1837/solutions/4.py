class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        Items = []
        for item in orders:
            if item[2] not in Items:
                Items.append(item[2])
                
        Items = [\"Table\"] + sorted(Items)
        
        dic = {}
        for table in orders:
            if table[1] not in dic:
                dic[table[1]] = [table[1]] + ['0']*(len(Items)-1)
        
        for order in orders:
            table = order[1]
            item = order[2]
            idx = Items.index(item)
            temp = int(dic[table][idx]) + 1
            dic[table][idx] = str(temp)
            
            
        temp = []
        for key in dic:
            temp.append(dic[key])
            
        ans = sorted(temp, key = lambda x: int(x[0]))
        
        return [Items] + ans
        
        
        
        
            
                
        
                
        
