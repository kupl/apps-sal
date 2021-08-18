class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        to_move = []
        num_moves = 0
        end = 50000

        for i in range(end):
            if count[i] >= 2:
                to_move.extend([i] * (count[i] - 1))
            elif to_move and count[i] == 0:
                num_moves += i - to_move.pop()

        return num_moves
