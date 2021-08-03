class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        m = 10000
        idx = defaultdict(int)
        l = []

        for i in range(len(A) - 1, -1, -1):
            if A[i] > m:
                l.sort()
                j = idx[l[bisect_left(l, A[i]) - 1]]
                A[i], A[j] = A[j], A[i]
                return A

            m = min(m, A[i])
            idx[A[i]] = i
            l.append(A[i])

        return A
