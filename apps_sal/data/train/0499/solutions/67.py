class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total = 0
        prev = 0
        for num in target:
            total += max(0, num - prev)
            prev = num
        return total
