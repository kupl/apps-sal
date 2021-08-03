class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans, prev = 0, 0
        for n in target:
            ans += max(0, n - prev)
            prev = n
        return ans
