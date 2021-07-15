class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        all_foods = set()
        all_tables = set()
        mapping = defaultdict()
        for order in orders:
            _, table_id, food_name = order[0], int(order[1]), order[2]
            all_foods.add(food_name)
            all_tables.add(table_id)
            if table_id not in mapping:
                mapping[table_id] = defaultdict(int) 
            mapping[table_id][food_name] += 1
            
        all_foods = sorted(list(all_foods))
        all_tables = sorted(list(all_tables))
        labels = ['Table'] + all_foods
        data_table = [labels]
        for table in all_tables:
            temp = [str(table)]
            for food in all_foods:
                temp.append(str(mapping[table][food]))
            
            data_table.append(temp.copy())
            
        return data_table

