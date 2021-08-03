class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = prev = 0
        for i in target:
            ans += max(0, i - prev)
            prev = i
        return ans
