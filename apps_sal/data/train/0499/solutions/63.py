class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        res = 0
        prev = 0
        for t in target:
            res += max(t - prev, 0)
            prev = t

        return res
