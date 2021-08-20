class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        cur = 0
        for i in range(len(target)):
            if target[i] > cur:
                res += target[i] - cur
            cur = target[i]
        return res
