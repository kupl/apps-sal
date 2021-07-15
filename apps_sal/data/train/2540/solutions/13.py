import numpy as np
class Solution:

#     def valid_area(self, A):
#         s = np.sum([a for a in A])/2
#         area = np.sqrt(s*(s-A[0])*(s-A[1])*(s-A[2]))
        
#         return False if np.isnan(area) or area == 0 else True
        
        
    def largestPerimeter(self, A: List[int]) -> int:
        
        valid_area = lambda x,y,z: True if x < y + z else False 
        A = sorted(A, reverse=True)
        for a in range(2,len(A)):
            if valid_area(A[a-2], A[a-1], A[a]): 
                return np.sum([A[a-2], A[a-1], A[a]])
        return 0
        
#         # greedy approach
#         comb = set([i for i in combinations(A,3)])
#         comb_sorted = sorted(comb, key=lambda x: np.sum(x), reverse=True)
#         for c in comb_sorted:
#             if self.valid_area(c):
#                 return np.sum(c)
            
#         return 0

