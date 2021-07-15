class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)        
        arr.sort()        
        m = arr[((n-1)//2)]
        
        arr.sort(key=lambda x: (abs(x-m),x), reverse=True)
        
        return arr[:k]
#         index = []        
        
#         for i in range(n):
#             index.append([abs(arr[i]-m), i, arr[i]])
        
#         index.sort(key=lambda x: (x[0],x[1]), reverse=True)
    
#         res = []
#         for j in range(k):
#             res.append(index[j][2])
        
#         return res

