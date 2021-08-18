class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        cols = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                cols[i][j] = matrix[j][i]

        for i in range(m):
            low, high = matrix[i][0], matrix[i][-1]
            if low <= target <= high:
                x = self.search(matrix[i], target)
                if target == matrix[i][x] or (0 < x <= len(matrix[i]) and target == self.search(cols[x], target)):
                    return True

        return False

    def search(self, arr, target):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] == target:
                return mid
            else:
                high = mid

        return low
