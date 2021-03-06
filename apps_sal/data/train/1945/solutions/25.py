class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        f = defaultdict(int)
        n = len(matrix[0])
        for i in matrix:
            (p, q) = ([], [])
            for j in range(n):
                if i[j] == 0:
                    p.append(j)
                else:
                    q.append(j)
            f[tuple(p)] += 1
            f[tuple(q)] += 1
        return max(f.values())
