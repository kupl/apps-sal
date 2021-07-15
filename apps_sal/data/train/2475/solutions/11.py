class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum([list(i) != sorted(i) for i in zip(*A)])
