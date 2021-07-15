class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ret = 0
        old = 0
        for e in target:
            if e > old:
                ret += e - old
            old = e
        return ret
