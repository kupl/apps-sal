class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i, j = 0, 0
        tempi, tempj = -100000, 100000
        flagi, flagj = True, True
        while i < len(A) and j < len(A):
            if tempi <= A[i]:
                tempi = A[i]
            else:
                flagi = False
            if tempj >= A[j]:
                tempj = A[j]
            else:
                flagj = False
            i += 1
            j += 1
        return flagi or flagj
