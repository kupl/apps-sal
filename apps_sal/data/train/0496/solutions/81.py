class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        n = {}

        def find(x):
            if x in n:
                n[x] = find(n[x] + 1)
            else:
                n[x] = x
            return n[x]
        ans = 0
        for a in A:
            ans += find(a) - a
        return ans
