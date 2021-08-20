class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        taken = []
        count = collections.Counter(A)
        moves = 0
        for i in range(100000):
            if count[i] >= 2:
                taken.extend([i] * (count[i] - 1))
            elif taken and count[i] == 0:
                moves += i - taken.pop()
        return moves
