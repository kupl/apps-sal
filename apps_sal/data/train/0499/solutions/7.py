class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        for i in range(1, len(target)):
            (pre, curr) = (target[i - 1], target[i])
            ans += max(curr - pre, 0)
        return ans + target[0]
