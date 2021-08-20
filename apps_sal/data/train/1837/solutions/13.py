class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_numbers = sorted(set([int(i[1]) for i in orders]))
        items = sorted(set([i[2] for i in orders]))
        temp_dict = {str(key): [0] * len(items) for key in table_numbers}
        for item in orders:
            temp_dict[item[1]][items.index(item[2])] = temp_dict[item[1]][items.index(item[2])] + 1
        result = [['Table'] + items]
        for (key, val) in temp_dict.items():
            result.append([key] + list(map(str, val)))
        return result
