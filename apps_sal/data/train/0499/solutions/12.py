class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum(max(0, a - b) for a, b in zip(target[1:], target))
