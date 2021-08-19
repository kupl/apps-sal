class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        result = 0
        for (index, value) in enumerate(target):
            if index == 0:
                result = value
            elif value > target[index - 1]:
                result += value - target[index - 1]
            pass
        return result
