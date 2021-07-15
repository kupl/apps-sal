class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        tot = 0
        l = 0
        for t in target:
            if t > l:
                tot += t - l
                l = t
            elif t < l:
                l = t
        return tot
