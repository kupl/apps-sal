class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = 0
        last = 0
        for i in range(len(target)):
            if target[i] >= last:
                result += target[i] - last
            last = target[i]
        return result
