class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        step = 0
        for i in range(len(target)):
            step += max(0, target[i] - prev)
            prev = target[i]
        return step
