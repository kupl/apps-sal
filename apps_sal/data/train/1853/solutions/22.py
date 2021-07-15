class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dij(arr, i):
            passed = [i]
            notpass = [j for j in range(len(arr)) if j != i ]
            dis = arr[i]
            while notpass:
                index = notpass[0]
                for node in notpass:
                    if dis[node] < dis[index]:
                        index = node
                passed.append(index)
                notpass.remove(index)
                
                for x, total in enumerate(dis):
                    dis[x] = min(dis[x], dis[index] + arr[index][x])
            return dis
                    
            
        arr = [[float('inf') for x in range(n)] for y in range(n)]  
        for i in range(n):
            arr[i][i] = 0
            
        for fromi, toj, val in edges:
            arr[fromi][toj] = val
            arr[toj][fromi] = val
            
        min_nums, min_indexes = float('inf'), []
        for i in range(n):
            dis = dij(arr, i)
            nums = len([length for length in dis if length <= distanceThreshold])
            if nums < min_nums:
                min_nums = nums
                min_indexes = [i]
            elif nums == min_nums:
                min_indexes.append(i)
                
        return max(min_indexes)
            

