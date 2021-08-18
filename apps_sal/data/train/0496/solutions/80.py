class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        n = {}
        ans = 0

        def find(j):
            n[j] = find(n[j] + 1) if j in n else j
            return n[j]

        for i in A:
            ans += find(i) - i
        return ans
