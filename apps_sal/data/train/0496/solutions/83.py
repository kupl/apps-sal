class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A = sorted(A)
        if not A:
            return 0
        k = A[0]
        moves = 0
        for i in range(1, len(A)):
            if A[i] <= k:
                moves += k + 1 - A[i]
                A[i] = k + 1
            k = A[i]
        return moves
