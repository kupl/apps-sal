class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        res = 0

        for i in range(len(target)):
            if i == 0:
                res = target[0]
                continue

            d = target[i] - target[i - 1]

            if d > 0:
                res += d

        return res
