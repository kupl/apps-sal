class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = []
        food = []
        for item in orders:
            table.append(int(item[1]))
            food.append(item[2])
        food = sorted(list(set(food)))
        table = sorted(list(set(table)))
        my_dict = {str(key): [0] * len(food) for key in table}
        for item in orders:
            my_dict[item[1]][food.index(item[2])] = my_dict[item[1]][food.index(item[2])] + 1
        header = ['Table'] + food
        footer = []
        for (key, val) in list(my_dict.items()):
            footer.append([key] + list(map(str, val)))
        return [header] + footer
