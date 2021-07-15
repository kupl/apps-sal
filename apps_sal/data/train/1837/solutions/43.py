class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = []
        dishes = []
        for name, table, dish in orders:
            if table not in tables:
                tables.append(table)
            if dish not in dishes:
                dishes.append(dish)
        tables = sorted(tables, key=lambda x: int(x))
        dishes = sorted(dishes)
        results = [[\"0\" for j in range(len(dishes) + 1)] for i in range(len(tables) + 1)]
        results[0] = [\"Table\"] + dishes
        for name, table, dish in orders:
            i = tables.index(table) + 1
            j = dishes.index(dish) + 1
            results[i][0] = table
            results[i][j] = str(int(results[i][j]) + 1)
        return results
