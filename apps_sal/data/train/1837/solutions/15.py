class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # runtime: O(nlogn + mlogm), where n = number of unique tables and m = # of unique foods
        # space: O(mn)
        foods = set()
        tables = set()
        for o in orders:
            tables.add(int(o[1]))
            foods.add(o[2])
        tables = sorted(tables)
        foods = sorted(foods)
        result = [([0] * (len(foods) + 1)) for i in range(len(tables) + 1)]
        # print(result)
        result[0][0] = \"Table\"
        reverse_foods = {}
        for i, food in enumerate(foods):
            result[0][i + 1] = food
            reverse_foods[food] = i + 1
        reverse_tables = {}
        for i, table in enumerate(tables):
            result[i + 1][0] = table
            reverse_tables[table] = i + 1
        for o in orders:
            result[reverse_tables[int(o[1])]][reverse_foods[o[2]]] += 1
        for i in range(1, len(result)):
            for j in range(len(result[0])):
                result[i][j] = str(result[i][j])
        return result
        
        
