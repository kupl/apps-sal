class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        res += target[0] - 1
        for i in range(1, len(target)):
            if target[i] <= target[i - 1]:
                continue
            else:
                res += target[i] - target[i - 1]
        return res + 1
