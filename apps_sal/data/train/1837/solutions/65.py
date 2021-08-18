class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        tableFood = {}
        Fooditems = set()
        for i in orders:
            if i[1] in list(tableFood.keys()):
                tableFood[i[1]].append(i[2])
            else:
                tableFood[i[1]] = [i[2]]
            Fooditems.add(i[2])

        Fooditems = list(Fooditems)
        Fooditems.sort()

        outTable = []

        for k, v in list(tableFood.items()):
            tmp = [k]
            for i in Fooditems:
                tmp.append(str(v.count(i)))
            outTable.append(tmp)

        outTable.sort(key=lambda outTable: int(outTable[0]))

        return [['Table'] + Fooditems] + outTable
