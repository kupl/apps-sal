class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        def sumMatrix(center: tuple):
            Sum = 0
            start_i = max(center[0] - K, 0)
            stop_i = min(center[0] + K + 1, len(mat[0]))
            start_j = max(center[1] - K, 0)
            stop_j = min(center[1] + K + 1, len(mat))
            for j in range(start_j, stop_j):
                Sum += sum(mat[j][start_i:stop_i])
            print('start_i', start_i, 'stop_i', stop_i, 'start_j', start_j, 'stop_j', stop_j)
            print('sum', Sum)
            return Sum
        res = []
        for i in range(len(mat)):
            res.append([])
            for j in range(len(mat[i])):
                res[i].append(sumMatrix((j, i)))
        return res
