class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        item_list = []
        order_dict = {}
        for order in orders:
            table = order[1]
            item = order[2]
            if item not in item_list:
                item_list.append(item)
            if int(table) not in order_dict:
                order_dict[int(table)] = []
            order_dict[int(table)].append(item)
        item_list.sort()
        item_list.insert(0, 'Table')
        order_dict = dict(sorted(order_dict.items()))
        sol = []
        sol.append(item_list)
        for (table_name, table_orders) in list(order_dict.items()):
            table_sol = ['0' for i in range(len(item_list))]
            table_sol[0] = table_name
            for order in table_orders:
                ind = item_list.index(order)
                table_sol[ind] = str(int(table_sol[ind]) + 1)
            sol.append(table_sol)
        for i in range(1, len(sol)):
            sol[i][0] = str(sol[i][0])
        return sol
