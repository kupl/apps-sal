from collections import defaultdict

class Solution:
    
    def tables_to_lists(self, tables):
        for table in tables:
            temp = tables[table]
            temp[0] = int(table)
            yield temp
            
    
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        all_foods = sorted(list(set(map(lambda x: x[2], orders))))
        all_foods.insert(0, \"Table\")
        
        result = []
        result.append(all_foods)
        
        
        tables = defaultdict(lambda: [0] * (len(all_foods)) )
        
        for order in orders:
            name, table, item = order
            tables[table][all_foods.index(item)] += 1
          
        subresult = [t for t in self.tables_to_lists(tables)]
        
        result.extend(sorted(subresult, key=lambda x: x[0]))
        
        for i in range(1, len(result)):
            result[i] = list(map(str, result[i]))
        
        return result
        
