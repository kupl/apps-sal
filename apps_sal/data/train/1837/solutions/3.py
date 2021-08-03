class Solution:
    def displayTable(self, orders):
        food, table = [0] * len(orders), [''] * len(orders)

        for i, item in enumerate(orders):
            table[i], food[i] = int(item[1]), item[2]

        food = sorted(set(food))
        table = sorted(set(table))

        dic = {str(key): [0] * len(food) for key in table}

        for item in orders:
            dic[item[1]][food.index(item[2])] += 1

        res = [['Table'] + food]
        for key, val in dic.items():
            res.append([key] + list(map(str, val)))

        return res
