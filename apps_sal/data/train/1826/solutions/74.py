class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        k = K

        def convolve(values):
            acc = sum(values[:k])
            result = []
            for i in range(len(values)):
                if i + k < len(values):
                    acc += values[i + k]
                if i - k - 1 >= 0:
                    acc -= values[i - k - 1]
                result.append(acc)
            return result

        def transpose(matrix):
            m = len(matrix)
            n = len(matrix[0])
            transposed = []
            for j in range(n):
                col = [matrix[i][j] for i in range(m)]
                row = col
                transposed.append(row)
            return transposed
        convolved_rows = [convolve(row) for row in mat]
        tranposed = transpose(convolved_rows)
        convolved = [convolve(row) for row in tranposed]
        return transpose(convolved)
