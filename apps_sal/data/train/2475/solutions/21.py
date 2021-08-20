class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for col in zip(*A):
            if list(col) != sorted(col):
                count += 1
        return count
