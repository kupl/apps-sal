class Solution:
    def numSubmat(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        h = [0] * n
        res = 0

        for i in range(m):

            stk = []
            psum = [0] * n

            for j in range(n):
                h[j] = h[j] + 1 if A[i][j] else 0

                while stk and h[stk[-1]] >= h[j]:
                    stk.pop()

                k = stk[-1] if stk else -1
                ksum = psum[k] if stk else 0

                psum[j] = ksum + h[j] * (j - k)

                stk.append(j)

            res += sum(psum)

        return res
