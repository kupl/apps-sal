from collections import defaultdict
# table nuber in string
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_set = set()
        table_orders = defaultdict(lambda : defaultdict(int))
        ans = []
        
        
        for ix, val in enumerate(orders):
            _ , table_no , food_name = val[0] , int(val[1]) , val[2]
            if table_no not in table_orders:
                table_orders[table_no][food_name] = 1
            else:
                # table number is inside
                table_orders[table_no][food_name] += 1
            food_set.add(food_name)
        
        
        temp = [\"Table\"]
        for food_name in sorted(food_set):
            temp.append(food_name)
        ans.append(temp)
        
        food_mapping = {}
        for ix in range(1,len(temp)):
            food_mapping[temp[ix]] = ix
        
        
        for table_num in sorted(table_orders.keys()):
            insert_list = [\"0\" for _ in range(len(food_mapping)+1)]
            insert_list[0] = str(table_num)
            order_dict = table_orders[table_num]
            for food_name in order_dict.keys():
                ix_add = food_mapping[food_name]
                insert_list[ix_add] = str(order_dict[food_name])
            ans.append(insert_list)
        return ans
            
            
