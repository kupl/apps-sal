class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        
#         food = dict()
        
#         for order in orders:
            
#             name, table, item = order[0], order[1], order[2]
            
#             if item not in food:
#                 food[item] = {}
#             if table not in food[item]:
#                 food[item][table] = 0
#             food[item][table] += 1
        
#         print(food)
#         dishes = [[\"Table\"] + sorted(food)]
        
#         print(dishes)
        
#         rowSize = len(dishes[0])
#         for i, f in enumerate(sorted(food)):
#             l = ['0'] * rowSize
#             tables = food[f]
#             for table in sorted(tables):
#                 l[0] = table
#                 l[i+1] = str(tables[table])
#             dishes.append(l)
#         print(dishes)
        
        tables = dict()
        
        foodSet = set()
        for order in orders:
            
            name, table, item = order[0], order[1], order[2]
            foodSet.add(item)
            if int(table) not in tables:
                tables[int(table)] = {}
            if item not in tables[int(table)]:
                tables[int(table)][item] = 0
            tables[int(table)][item] += 1
        
        row = [\"Table\"] + sorted(foodSet)
        dishes = [row]
        index = dict()
        
        for i, r in enumerate(row):
            index[r] = i
            
        rowSize = len(dishes[0])
        
        for table in sorted(tables):
     
            foods = tables[table]
            l = [\"0\"] * rowSize
            l[0] = str(table)
            for food in sorted(foods):
                l[index[food]] = str(foods[food])
       
            dishes.append(l)
        return dishes
        
