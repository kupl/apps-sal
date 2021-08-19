class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])

        def sunmat(sr, sc):
            maxc = C
            count = 0
            for x in range(sr, R):
                for y in range(sc, maxc):
                    if mat[x][y] == 1:
                        count += 1
                    else:
                        maxc = y
                        break
            return count
        res = 0
        for x in range(R):
            for y in range(C):
                if mat[x][y] == 0:
                    continue
                res += sunmat(x, y)
        return res
