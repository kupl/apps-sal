class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.search(matrix, target)

    def use_binary_search(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        (m, n) = (len(matrix), len(matrix[0]))
        for i in range(m):
            if self.binary_search(matrix, target, i, False):
                return True
        for i in range(n):
            if self.binary_search(matrix, target, i, True):
                return True
        return False

    def binary_search(self, matrix, target, start, vertical):
        lo = 0
        hi = len(matrix) if vertical else len(matrix[0])
        while lo < hi:
            mid = lo + (hi - lo) // 2
            val = matrix[mid][start] if vertical else matrix[start][mid]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid
        return False

    def search(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        (m, n) = (len(matrix), len(matrix[0]))
        (row, col) = (m - 1, 0)
        while row >= 0 and col < n:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                row -= 1
            else:
                col += 1
        return False
