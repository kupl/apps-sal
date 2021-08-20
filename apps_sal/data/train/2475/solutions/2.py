class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        if len(A) <= 1:
            return 0
        elif len(A[1]) == 1:
            return 0
        D = []
        for i in range(0, len(A[0])):
            col = [a[i] for a in A]
            col_sort = sorted(col)
            if col != col_sort:
                D.append(i)
        return len(D)
