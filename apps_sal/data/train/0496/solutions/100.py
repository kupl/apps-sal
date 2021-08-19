class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        if A == []:
            return 0
        else:
            A.sort()
            pre_item = A[0]
            moves = 0
            for i in range(1, len(A)):
                cur_item = A[i]
                if A[i] < pre_item or A[i] == pre_item:
                    moves = moves + pre_item + 1 - A[i]
                    A[i] = pre_item + 1
                pre_item = A[i]
            return moves
