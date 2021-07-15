import collections
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res, need = 0, 0
        numCnt = collections.OrderedDict()
        for a in A:
            if a not in numCnt:
                numCnt[a] = 1
            else:
                numCnt[a] += 1
        while numCnt:
            num, count = numCnt.popitem(last=False)
            res += max((need - num)*count, 0) + count*(count-1)//2
            need = max(num, need) + count
            
        return res
