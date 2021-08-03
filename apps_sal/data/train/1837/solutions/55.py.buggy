class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set([])
        table_idx_to_orders = {} 
        
        for order in orders:
            food = order[2]
            if food not in foods:
                foods.add(food)
                        
        foods_list = sorted(list(foods))
        total_foods = len(foods_list)
        food_to_idx = { foods_list[i] : i for i in range(len(foods_list)) }
        for order in orders:
            _, table_idx, food = order
            table_idx = int(table_idx)
            if table_idx not in table_idx_to_orders:
                table_idx_to_orders[table_idx] = [0] * total_foods
                
            table_idx_to_orders[table_idx][food_to_idx[food]] += 1
            
        result = [[\"Table\"] + list(food_to_idx)]
        print(table_idx_to_orders)
        for table_idx in sorted(table_idx_to_orders.keys()):
            print(table_idx)
            crt_orders_str = list(map(str, list(table_idx_to_orders[table_idx])))
            crt_result = [str(table_idx)] + crt_orders_str
            result.append(crt_result)
        return result
        
        
