from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        table_to_dishes = defaultdict(lambda: defaultdict(int))
        dishes = set()

        for order in orders:
            table = int(order[1])
            dish = order[2]

            table_to_dishes[table][dish] += 1
            dishes.add(dish)

        headers = ['Table']
        headers += [dish for dish in sorted(dishes)]

        result = [headers]

        for table in sorted(table_to_dishes.keys()):
            table_order = [str(table)]

            for ind in range(1, len(headers)):
                dish = headers[ind]
                table_order.append(str(table_to_dishes[table][dish]))

            result.append(table_order)

        return result
