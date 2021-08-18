class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        '''
        Time: O(mn)
        Space: O(n + n) ~ O(n)
        '''
        m = len(arr)
        n = len(arr[0])

        if m == 1:
            return arr[0][0]

        def get_min_neighbors(i, j):
            a, row_prev[j] = row_prev[j], float('inf')
            min_val = min(row_prev)
            row_prev[j] = a
            return min_val

        row_prev = arr[0]
        cur = [0] * n
        global_min = float('inf')

        for row in range(1, m):
            for col in range(n):
                cur[col] = get_min_neighbors(row, col) + arr[row][col]

                if row == m - 1 and cur[col] < global_min:
                    global_min = cur[col]

            row_prev = cur[:]

        return global_min
