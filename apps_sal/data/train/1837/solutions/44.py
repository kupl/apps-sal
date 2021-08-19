class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        orders.sort(key=lambda x: int(x[1]))
        record = defaultdict(lambda: defaultdict(int))
        foods = []
        for (name, table, food) in orders:
            if food not in foods:
                foods.append(food)
            record[table][food] += 1
        foods = sorted(foods)
        out = [['Table'] + foods]
        for (k, v) in record.items():
            tmp = [k]
            for f in foods:
                tmp += [str(v.get(f)) if v.get(f) else '0']
            out.append(tmp)
        return out
