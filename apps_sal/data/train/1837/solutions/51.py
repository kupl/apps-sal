from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tableFood = {}
        tableFreq = {}
        foods = set()
        nums = set()
        for order in orders:
            tableNumber = order[1]
            food = order[2]
            foods.add(food)
            nums.add(tableNumber)
            idx = (tableNumber, food)
            
            
            if idx in tableFreq:
                tableFreq[idx] += 1
            else:
                tableFreq[idx] = 1
        
        cols = [\"Table\"] + sorted(foods)
        ans = [cols]
        N = len(cols)
        
        sortedKeys = sorted(nums, key = lambda k: int(k))
        
        for key in sortedKeys:
            col = [\"0\"] * N
            col[0] = key
            for i in range(1,N):
                idx = (key,cols[i])
                if idx in tableFreq:
                    col[i] = str(tableFreq[idx])
            ans.append(col)

        return ans
            
            
            
                
            
            
            
            
            
        
