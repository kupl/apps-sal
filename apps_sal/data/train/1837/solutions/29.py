class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        tables = {}
        menu = set()

        for o in orders:
            num, food = int(o[1]), o[2]

            if num not in tables:
                tables[num] = {}

            if food not in tables[num]:
                tables[num][food] = 0

            tables[num][food] += 1

            if food not in menu:
                menu.add(food)

        menu = sorted(menu)
        res = [['Table'] + menu]

        for table_num in sorted(tables, key=lambda n: n):
            row = [str(table_num)]
            table_order = tables[table_num]

            for food in menu:
                food_count = table_order.get(food, 0)
                row.append(str(food_count))
            res.append(row)

        return res
