class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = 0
        if not target:
            return result
        result = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                result += target[i] - target[i - 1]
        return result
