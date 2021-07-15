class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food, table = [0]*len(orders), ['']*len(orders)
        #print(food, table)
        
        for i, item in enumerate(orders):
            table[i], food[i] = int(item[1]), item[2]
        #print(food, table)
        
        food = sorted(set(food))
        table = sorted(set(table))
        #print(food, table)
        
        my_dict = {}
        for i in table:
            my_dict[str(i)] = [0]*len(food)
        #print(my_dict)
        
        for item in orders:
            my_dict[item[1]][food.index(item[2])] += 1
        #print(my_dict)
        
        result = [['Table'] + food]
        for key, val in my_dict.items():
            result.append([key]+list(map(str,val)))
        
        return result
