class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # two pointers to traverse array checking increasing and decreasing at the same time.
        i, j = 0, 0
        # two variables to keep track of values increasing and decreasing.
        tempi, tempj = -100000, 100000
        # flag to check if monotonic.
        flagi, flagj = True, True
        # go through array, check if monotonic.
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
        # return True by default.
        return flagi or flagj
