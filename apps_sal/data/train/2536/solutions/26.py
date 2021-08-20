class Solution:

    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        max = 0
        for (k, v) in list(d.items()):
            if k == v:
                if v > max:
                    max = v
        if max != 0:
            return max
        else:
            return -1
