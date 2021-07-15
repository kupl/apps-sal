class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) < 2:
            return 0
        A.sort()
        ans, last = 0, A[0]-1
        for n in A:
            if n > last:
                last = n
            else:
                ans += (last-n+1)
                last += 1
        return ans

