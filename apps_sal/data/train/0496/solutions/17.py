class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        seen = []
        res = 0
        for x in range(100000):
            if count[x] >= 2:
                seen.extend([x] * (count[x] - 1))
            elif seen and count[x] == 0:
                res += x - seen.pop()
        return res
