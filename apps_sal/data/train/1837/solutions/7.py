class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        keys, table = [], []
        for order in orders:
            keys.append(order[2])
            table.append(int(order[1]))
        keys = sorted(set(keys))
        table = [str(i) for i in sorted(set(table))] 
        d = {t : {k : 0 for k in keys} for t in table}
        for order in orders:
            d[order[1]][order[2]] += 1
        ans = [[\"Table\"] + keys]
        for tab in table:
            temp = [tab]
            for food in keys:
                temp.append(str(d[tab][food]))
            ans.append(temp)
        return ans
