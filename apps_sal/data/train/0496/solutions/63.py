class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        seen = set()
        replicates = []
        for i in A:
            if i not in seen:
                seen.add(i)
            else:
                replicates.append(i)
        replicates.sort()
        res = 0
        next_candidates = 0
        while replicates:
            num = replicates.pop(0)
            next_candidates = max(next_candidates, num)
            while next_candidates in seen:
                next_candidates += 1
            seen.add(next_candidates)
            res += next_candidates - num
        return res
