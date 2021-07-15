class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ret = target[0]
        for i in range(1, len(target)):
            ret += max(0, target[i] - target[i-1])
        return ret
