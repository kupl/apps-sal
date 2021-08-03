class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        for i in range(len(A)):
            A[i] = sorted(list(A[i][::2])) + sorted(list(A[i][1::2]))
        A.sort()
        n = 0
        while len(A) > 0:
            A = A[A.count(A[0]):]
            n += 1
        return n
