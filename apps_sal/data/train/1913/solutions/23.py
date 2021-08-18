class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 2, -1, -1):
            ans = (-1, -1)
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    ans = max(ans, (A[j], -j))
            if ans[0] != -1:
                A[i], A[-ans[1]] = A[-ans[1]], A[i]
                return A
        return A
