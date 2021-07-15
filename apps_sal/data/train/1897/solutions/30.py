class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        res = []
        for q in queries:
            res.append(arr[q[1]] ^ (0 if q[0] <= 0 else arr[q[0]-1]))
        return res
