class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        num_increments = 0
        prev = 0
        for t in target:
            if t > prev:
                num_increments += t - prev
            prev = t
        return num_increments
