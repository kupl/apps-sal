class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N + 1) / 2:
                return ""
            A.extend(c * x)
            print(A)
        ans = [None] * N
        ans[::2], ans[1::2] = A[int(N / 2):], A[:int(N / 2)]
        print(ans[::2])
        return "".join(ans)
