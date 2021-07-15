class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # A[i] is non negative 
        seen = set()
        replicates = []
        for i in A: #O(n)
            if i not in seen:
                seen.add(i)
            else:
                replicates.append(i)
        replicates.sort() #O(nlogn)
        res = 0
        next_candidates = 0
        while replicates: #O(n)
            num = replicates.pop(0)
            next_candidates = max(next_candidates, num)
            while next_candidates in seen:
                next_candidates += 1 
            seen.add(next_candidates)
            res += next_candidates - num 
        return res 
