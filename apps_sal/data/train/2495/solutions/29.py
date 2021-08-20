class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d1 = {}
        d2 = {}
        for i in target:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in arr:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        for (k, v) in d1.items():
            if k not in d2:
                return False
            elif v != d2[k]:
                return False
        return True
