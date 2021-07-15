class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = target[0]
        for a, b in zip(target, target[1:]):
            count += max(0, b - a)
        return count
