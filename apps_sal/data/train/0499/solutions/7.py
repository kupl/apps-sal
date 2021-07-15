class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # target[0] + sum([max(0, curr - pre) for pre, curr in zip(target, target[1:])])
        # if len(target) == 1: return target[0]
        ans = 0
        for i in range(1, len(target)):
            pre, curr = target[i-1], target[i]
            ans += max(curr-pre, 0)
        return ans + target[0]
