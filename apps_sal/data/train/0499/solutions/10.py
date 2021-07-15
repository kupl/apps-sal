class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum([max(0, curr - pre) for pre, curr in zip(target, target[1:])])
