class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target: return 0
        ret = target[0]
        for a,b in zip(target[:-1], target[1:]):
            ret += max(0, b-a)
        return ret

