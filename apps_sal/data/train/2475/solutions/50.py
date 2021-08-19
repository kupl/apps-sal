class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for i in range(0, len(A[0])):
            maximum = A[0][i]
            inDecreasingOrder = True
            j = 1
            while j < len(A):
                val = A[j][i]
                if val < maximum:
                    inDecreasingOrder = False
                    break
                maximum = val
                j += 1
            if inDecreasingOrder:
                count += 1
        return len(A[0]) - count
