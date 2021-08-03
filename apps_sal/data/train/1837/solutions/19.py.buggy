
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = set()
        
        for _, table, food in orders:
            foods.add(food)
            tables.add(table)
        
        foodcounts = {f:{t:0 for t in tables} for f in foods}
        for _, table, food in orders:
            foodcounts[food][table] += 1
            
        output = []
        output.append([\"Table\"] + sorted(foods))
        for table in sorted(map(int,tables)):
            table = str(table)
            counts = [table]
            for food in sorted(foods):
                counts.append(str(foodcounts[food][table]))
            output.append(counts)
        return output
        
