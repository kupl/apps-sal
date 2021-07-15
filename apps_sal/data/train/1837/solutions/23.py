# Dict of Dicts For food counts on a table
#   tables[5][\"Ceviche\"] = 1
# Set unique foods
# 1. Time O(N) Space: O(N)
# 2. Time O(I*J)

from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        table_foods = defaultdict(lambda: defaultdict(int))
        unique_food = set()
        
        for _, table_number, food in orders:
            table_foods[int(table_number)][food] += 1
            unique_food.add(food)
        
        headers = sorted(unique_food)
        data = [[\"Table\"] + headers]
        
        for table_number in sorted(table_foods.keys()):
            table_row = [str(table_number)]
            for food in headers:
                table_row.append(str(table_foods[table_number][food]))
            data.append(table_row)
        return data

    
