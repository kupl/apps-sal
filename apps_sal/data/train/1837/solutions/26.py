from collections import defaultdict


class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        result = []
        table_dct = defaultdict(list)
        items = set()
        tables = set()
        for order in orders:
            table_dct[order[1]].append(order[2])
            items.add(order[2])
            tables.add(int(order[1]))
        items = sorted(list(items))
        tables = sorted(list(tables))
        result.append(['Table'] + items)
        for table in tables:
            table_result = [str(table)]
            for item in items:
                table_result.append(str(table_dct[str(table)].count(item)))
            result.append(table_result)
        return result
