class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        delete_size = 0
        cols = zip(*A)
        for col in cols:
            for (a, b) in zip(col, col[1:]):
                if a > b:
                    delete_size += 1
                    break
        return delete_size
