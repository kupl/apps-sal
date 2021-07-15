class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = {}
        foods = set()
        
        for x in orders:
            table = x[1]
            food = x[2]
            foods.add(food)
            
            if table not in d:
                d[table] = {}
                
            if food in d[table]:
                d[table][food] +=1 
            else:
                d[table][food] = 1
                
        print(d)
        
        foodList = list(foods)
        foodList.sort()
        foodList.insert(0,'Table')
        
        hold = foodList
        f = [hold.copy()]
        dTemp = sorted(list(d.items()),key=lambda x:int(x[0]))
        for (tableNo,tableFood) in dTemp:
            a = []
            for colName in hold:
                if colName == 'Table':
                    a.append(str(tableNo))
                elif colName in tableFood:
                    a.append(str(tableFood[colName]))
                else:
                    a.append('0')
            f.append(a)
            
        
        return f
                
                

