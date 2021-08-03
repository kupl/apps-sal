class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food, table = [0] * len(orders), [''] * len(orders)

        for i, item in enumerate(orders):
            table[i], food[i] = int(item[1]), item[2]

        food = sorted(set(food))
        table = sorted(set(table))

        my_dict = {str(key): [0] * len(food) for key in table}

        for item in orders:
            my_dict[item[1]][food.index(item[2])] += 1

        result = [['Table'] + food]
        for key, val in my_dict.items():
            result.append([key] + list(map(str, val)))

        return result
