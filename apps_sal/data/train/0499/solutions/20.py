class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        l = len(target)
        if l == 1:
            return target[0]
        ans = target[0]
        for i in range(1, l):
            if target[i] > target[i - 1]:
                ans += target[i] - target[i - 1]
        return ans
