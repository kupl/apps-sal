class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dishes = []
        dishesSet = set()
        tables = []
        tableSet = set()
        
        orderDict = {}
        
        for order in orders:
            tableID = int(order[1])
            
            if tableID not in tableSet:
                tableSet.add(tableID)
                tables.append(tableID)
                orderDict[tableID] = {}
            
            if order[2] not in dishesSet:
                dishesSet.add(order[2])
                dishes.append(order[2])
            
            orderDict[tableID][order[2]] = orderDict[tableID].get(order[2], 0) + 1
        
        dishes.sort()
        tables.sort()
            
        orderTable = [[\"Table\"] + dishes]
        
        for table in tables:
            curr = []
            curr.append(str(table))
            for dish in dishes:
                if dish in orderDict[table]:
                    curr.append(str(orderDict[table][dish]))
                else:
                    curr.append(\"0\")
            
            orderTable.append(curr)
        
        return orderTable
        
        
        
