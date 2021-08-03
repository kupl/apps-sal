class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        col = 0
        while col < len(A[0]):
            row = 0
            while row < len(A) - 1:
                if ord(A[row][col]) > ord(A[row + 1][col]):
                    count += 1
                    break
                row += 1
            col += 1
        return count
