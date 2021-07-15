class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        
        ind = 0
        
        for a,b,c in trips:
            
            ind = max(ind, b, c)
            
        res = [0] * (ind+1)
        
        for a, b, c in trips:
            
            for i in range(b, c):
                res[i] += a
        return not any([x > capacity for x in res])
        
        
            
            
            
        
#         trips.sort(key=lambda x: (x[1], x[2]))
        
#         print(trips)
        
#         pas, start, end = trips[0]
        
#         for i in range(1, len(trips)):
            
#             if trips[i][1] < end:
                
#                 pas += trips[i][0]
#                 if pas > capacity:
#                     return False
#                 end = max(end, trips[i][2])
#             else:
#                 pas = trips[i][0]
#         return True

