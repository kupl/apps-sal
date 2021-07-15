class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        table = []
        table.append(\"Table\")
        res = []
        final_ans = []
        dict = {}
        
        dish_list = []
        for dish in orders:
            if dish[2] not in dish_list:
                dish_list.append(dish[2])
        
        dish_list.sort()
        
        
        for i in range(0, len(dish_list)):
            dict[dish_list[i]] = []
            table.append(dish_list[i])
            
        final_ans.append(table)
        
        for i in range(0, len(orders)):
            dict[orders[i][2]].append(orders[i][1])
       
        table_nos = []
        for num in orders:
            if int(num[1]) not in table_nos:
                table_nos.append(int(num[1]))
        
        table_nos.sort()
        
        for i in range(0, len(table_nos)):
            op = []
            op.append(str(table_nos[i]))
            for key in dict:
                op.append(str(dict[key].count(str(table_nos[i]))))
                
                
            if op not in res:
                res.append(op)
        
        for x in res:
            final_ans.append(x)
            
        return final_ans
