class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        hm = {}
        food = sorted(set([x[2] for x in orders]))
        tables = sorted(set([int(x[1]) for x in orders]))
        res = [['Table'] + list(food)] + [[str(x)] for x in tables]
        for item in orders:
            cur = hm.get(item[1], {})
            num = cur.get(item[2], 0)
            cur[item[2]] = num + 1
            hm[item[1]] = cur
        for i in range(1, len(tables) + 1):
            cur = hm[str(tables[i - 1])]
            for f in food:
                res[i].append(str(cur.get(f, 0)))
        return res
