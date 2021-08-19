class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        length = len(A[0])
        noofstr = len(A)
        print(length, noofstr)
        for i in range(length):
            increasing = True
            for j in range(1, noofstr):
                if A[j][i] < A[j - 1][i]:
                    increasing = False
                    break
            if increasing:
                count += 1
        return length - count
