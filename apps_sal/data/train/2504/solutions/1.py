class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i, j in enumerate(arr):
            ans += ((i + 1) * (n - i) + 1) // 2 * j
        return ans
