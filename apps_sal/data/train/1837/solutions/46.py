class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ss = set()
        for (x, y, z) in orders:
            ss.add(z)
        foods = list(ss)
        foods.sort()
        foodHt = {v:i for (i, v) in enumerate(foods)}
        ans = []
        firstRow = [\"Table\"] + foods
        ans.append(firstRow)
        
        ht = {}
        for x, y, z in orders:
            if not y in ht:
                ht[y] = [0 for i in range(len(foods))]
            ht[y][foodHt[z]] += 1
        
        tables = list(ht.keys())
        tables.sort(key=lambda x :int(x))
        for t in tables:
            row = [str(t)]
            for i in range(len(foods)):
                row.append(str(ht[t][i]))
            ans.append(row)
        return ans
