class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        M = len(mat)
        N = len(mat[0])

        def get_sum(i, j):

            def get_range(v, lim):
                return [x for x in range(v - K, v + K + 1) if x >= 0 and x < lim]
            ir = get_range(i, M)
            jr = get_range(j, N)
            return sum([mat[x][y] for x in ir for y in jr])
        res = []
        for i in range(len(mat)):
            res.append([])
            for j in range(len(mat[i])):
                res[i].append(get_sum(i, j))
        return res
