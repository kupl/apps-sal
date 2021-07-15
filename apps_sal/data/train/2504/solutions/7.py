class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        
        for k in range(1, n + 1, 2):
            for i, v in enumerate(arr):
                res += v * min(n - k + 1, k, i + 1, n - i)
        
        return res
