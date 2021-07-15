
class Solution:
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        squared = [round((x[0]**2 + x[1]**2)**(1/2),2) for x in points]
        self.heapSort(points, squared)
        result = []
        
        for i in range(K):
            result.append(points[i])
        return result
    
    def heapify(self, points, squared, n, i):
        
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and squared[l] > squared[largest]:
            largest = l
        
        if r < n and squared[r] > squared[largest]:
            largest = r
            
        if largest != i:
            squared[largest], squared[i] = squared[i], squared[largest]
            points[largest], points[i] = points[i], points[largest]
            
            self.heapify(points, squared, n, largest)
            
    def heapSort(self, points, squared):
        n = len(squared)
        
        for i in range( n // 2 - 1, -1, -1):
            self.heapify(points, squared, n, i)
            
        for i in range(n-1, 0, -1):
            squared[i], squared[0] = squared[0], squared[i]
            points[i], points[0] = points[0], points[i]
            self.heapify(points, squared, i, 0)
            
        # Solution_1
#         min_dist = []
        
#         def calculate_sqrt(x):
#             return round(math.sqrt(x[0]**2 + x[1]**2), 2)
        
#         for i in range(0, len(points)):
            
#             min_dist.append((calculate_sqrt(points[i]), points[i]))
        
#         min_dist = sorted(min_dist)
        
       
        
        
#         return [min_dist[i][1] for i in range(K) ]

