from collections import defaultdict


class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        to_merge = []
        moves = 0
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                to_merge.append(A[i])
            elif to_merge:
                j = A[i - 1]
                for j in range(A[i - 1] + 1, A[i]):
                    m = to_merge.pop(0)
                    moves += j - m
                    if not to_merge:
                        break
        if to_merge:
            j = A[-1] + 1
            while to_merge:
                m = to_merge.pop(0)
                moves += j - m
                j += 1
        return moves
