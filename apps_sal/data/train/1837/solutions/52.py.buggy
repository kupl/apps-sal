from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_items = set()
        tables = defaultdict(lambda: defaultdict(int))
        
        for o in orders:
            table_number = int(o[1])
            food_item = o[2]
            tables[table_number][food_item] += 1
            food_items.add(food_item)
            
        food_items = sorted(food_items)
        result = [[\"Table\"]]
        for food_item in food_items:
            result[0].append(food_item)
            
        for table_number in sorted(tables.keys()):
            record = [str(table_number)]            
            for food_item in food_items:
                record.append(str(tables[table_number][food_item]))
            result.append(record)
                
        return result
        
