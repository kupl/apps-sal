class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(max(A) - min(A) - 2 * K, 0)
#         min_val = max_val = A[0]
        
#         for a in A:
#             if a < min_val: min_val = a
#             elif a > max_val: max_val = a
#             # min_val = min(min_val, a)
#             # max_val = max(max_val, a)
        
#         return max(max_val - min_val - 2 * K, 0)  
        

