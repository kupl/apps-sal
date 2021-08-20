class Solution:

    def histogramCount(self, histograms):
        stack = []
        count = 0
        out = 0
        for i in range(len(histograms)):
            while len(stack) != 0 and histograms[i] < histograms[stack[-1]]:
                j = stack.pop()
                if len(stack) == 0:
                    k = -1
                else:
                    k = stack[-1]
                count -= (histograms[j] - histograms[i]) * (j - k)
            count += histograms[i]
            out += count
            stack.append(i)
        return out

    def numSubmatHard(self, mat: List[List[int]]) -> int:
        prev = [0] * len(mat[0])
        out = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    prev[j] = 0
                else:
                    prev[j] += mat[i][j]
            out += self.histogramCount(prev)
            print(prev, out)
        return out

    def memoization(self, grid, i, j, memo):
        if i == len(grid) or j == len(grid[0]):
            return (0, 0, 0)
        if memo[i][j] is not None:
            return memo[i][j]
        if grid[i][j] == 0:
            memo[i][j] = (0, 0, 0)
        elif i == len(grid) - 1:
            (_, col, _) = self.memoization(grid, i, j + 1, memo)
            memo[i][j] = (1, col + 1, col + 1)
        elif j == len(grid[0]) - 1:
            (row, _, _) = self.memoization(grid, i + 1, j, memo)
            memo[i][j] = (row + 1, 1, row + 1)
        else:
            (rows, _, _) = self.memoization(grid, i + 1, j, memo)
            prev = rows + 1
            out = prev
            k = j + 1
            while k < len(grid[0]) and grid[i][k] != 0:
                (row, _, _) = self.memoization(grid, i, k, memo)
                prev = min(prev, row)
                out += prev
                k += 1
            memo[i][j] = (rows + 1, k - j, out)
        return memo[i][j]

    def numSubmat(self, mat: List[List[int]]) -> int:
        memo = [[None for j in range(len(mat[0]))] for i in range(len(mat))]
        out = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                (_, _, val) = self.memoization(mat, i, j, memo)
                out += val
        return out
