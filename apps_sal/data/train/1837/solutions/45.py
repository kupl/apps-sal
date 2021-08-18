class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ht1 = {}
        col = []
        display = []

        for i, item in enumerate(orders):
            table = int(item[1])
            dish = item[2]
            if table in ht1:
                ht1[table].append(i)
            else:
                ht1[table] = [i]

            if dish not in col:
                col.append(dish)

        row = list(ht1.keys())
        row.sort()
        col.sort()

        display = [[]] * (len(row) + 1)
        display[0] = ['Table']
        for item in col:
            display[0].append(item)

        for i, item in enumerate(row):
            display[i + 1] = [str(item)]
            for j in range(len(col)):
                display[i + 1].append(0)
            for o in ht1[item]:
                dish = orders[o][2]
                c = col.index(dish)
                display[i + 1][c + 1] += 1
            for j in range(len(col)):
                display[i + 1][j + 1] = str(display[i + 1][j + 1])
        return display
