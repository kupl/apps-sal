class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = collections.defaultdict(dict)
        food = set()
        for _, i, j in orders:
            table[i][j] = table[i].get(j, 0) + 1
            food.add(j)

        res = [['Table'] + sorted(food)]
        for i in sorted(table, key=lambda x: int(x)):
            tmp = [str(i)]
            for j in range(1, len(res[0])):
                tmp.append(str(table[str(i)].get(res[0][j], 0)))
            res.append(tmp)

        return res
