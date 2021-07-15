class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        table = {}
        dishes = set()
        
        for order in orders:
            if order[1] not in table:
                table[order[1]] = {}
                
            if order[2] not in table[order[1]]:
                table[order[1]][order[2]] = 1
            else:
                table[order[1]][order[2]] += 1
                
            dishes.add(order[2])
            
        dishes = sorted(list(dishes))
        table_ints = [int(x) for x in table.keys()]
        table_nums = sorted(table_ints, reverse=False)
        
        template = [\"Table\"] + dishes
        display = [template]
        for num in table_nums:
            order = [str(num)]
            for dish in dishes:
                order.append(str(table.get(str(num), {}).get(dish, 0)))
                
            display.append(order)
            
        return display
