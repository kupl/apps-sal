class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = {}
        dishes = {}
        for name, table, dish in orders:
            if table not in tables:
                tables[table] = 0
            if dish not in dishes:
                dishes[dish] = 0
        tables = sorted(tables.keys(), key=lambda x: int(x))
        dishes = sorted(dishes.keys())
        tables.insert(0, 'Table')
        dishes.insert(0, 'Table')
        nrows = len(tables)
        ncolumns = len(dishes)
        
        results = [[0 for j in range(ncolumns)] for i in range(nrows)]
        results[0] = dishes
        tables = {table:index for index, table in enumerate(tables)}
        dishes = {dish:index for index, dish in enumerate(dishes)}

        for name, table, dish in orders:
            i = tables[table]# + 1
            j = dishes[dish]# + 1
            results[i][0] = table
            results[i][j] = results[i][j] + 1
        #print(results)
        for i in range(nrows):
            for j in range(ncolumns):
                results[i][j] = str(results[i][j])
        return results
