from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = defaultdict(lambda: defaultdict(int))
        foods = set()
        for _, table, order in orders:
            d[int(table)][order] += 1
            foods.add(order)
        foods = sorted(foods)
        ret = [['Table'] + foods]
        for table in sorted(d.keys()):
            ret.append([str(table)] + [str(d[table][f]) for f in foods])
        return ret
