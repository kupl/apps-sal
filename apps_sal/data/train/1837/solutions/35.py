class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        menu = sorted(set([i[2] for i in orders]))
        wat = sorted(orders, key=lambda order: int(order[1]))
        wat2 = itertools.groupby(wat, key=lambda order: order[1])
        alpha_cust = [[c, [i[2] for i in cgen]] for (c, cgen) in wat2]
        ans = [['Table'] + menu]
        for table in alpha_cust:
            ans.append([table[0]] + [str(table[1].count(i)) for i in menu])
        return ans
