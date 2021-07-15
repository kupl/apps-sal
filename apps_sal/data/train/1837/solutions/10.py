class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tableOrders = defaultdict(lambda: defaultdict(int))
        for order in orders:
            name,table,food = order
            tableOrders[table][food] += 1
        
        foods = set()
        for table in tableOrders:
            for key in tableOrders[table]:
                foods.add(key)
        foods = sorted(list(foods))
        tables = sorted(list(tableOrders.keys()),key=lambda x: int(x))
        # print(tables)
        result = [[\"Table\"]+foods]
        for table in tables:
            toAppend = [table]
            for food in foods:
                toAppend.append(str(tableOrders[table][food]))
            result.append(toAppend)
        return result
