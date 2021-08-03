class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = {}
        fooditems = []
        for order in orders:
            if order[1] in table:
                table[order[1]][order[2]] = table[order[1]].get(order[2],0) + 1
            
            else:
                table[order[1]] = {}
                table[order[1]][order[2]] = 1
     
            fooditems.append(order[2])
            
        fooditems = sorted(list(set(fooditems)))

        row = [[\"Table\"] + fooditems]
      
        for o in sorted(table.keys(), key=lambda x:int(x)):
         
            r = [o] + [str(table[o].get(food,0)) for food in fooditems]
            row.append(r)
            
        return row   
        
