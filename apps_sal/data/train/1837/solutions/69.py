class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = collections.defaultdict(lambda: collections.defaultdict(int))
        foods = set()
        for _, table, food in orders:
            foods.add(food)
            d[int(table)][food] += 1

        res = [[0] * (len(foods) + 1) for _ in range(len(list(d.keys())) + 1)]
        columns = {food: i + 1 for i, food in enumerate(sorted(foods))}
        res[0] = ['Table'] + sorted(foods)
        for i, table in enumerate(sorted(d.keys())):
            res[i + 1][0] = table
            for food in d[table]:
                res[i + 1][columns[food]] += d[table][food]
        return [list(map(str, x)) for x in res]
