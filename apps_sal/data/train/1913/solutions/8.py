class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if sorted(A) == A:
            return A

        n = len(A)
        s = A[:]
        for i in range(n - 2, -1, -1):
            s[i] = min(s[i], s[i + 1])
            if A[i] > s[i + 1]:
                j = n - 1
                while A[j] >= A[i]:
                    j -= 1
                A[i], A[j] = A[j], A[i]
                return A
