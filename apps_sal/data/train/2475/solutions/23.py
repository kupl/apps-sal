class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        rows = len(A)
        cols = len(A[0])
        out = []
        for i in range(cols):
            temp = []
            for j in range(rows):
                temp.append(A[j][i])
            out.append(temp)
        count = 0
        for i in out:
            if i != sorted(i):
                count += 1
        return count
