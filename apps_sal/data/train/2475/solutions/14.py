class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(not all(c <= d for c, d in zip(col, col[1:])) for col in zip(*A))

