class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        ret = 0
        height = [0] * n
        for i in range(m):
            for j in range(n):
                height[j] = 0 if not mat[i][j] else height[j] + 1
                if mat[i][j]:
                    h = height[j]
                    for k in range(j, -1, -1):
                        if mat[i][k]:
                            h = min(h, height[k])
                            ret += h
                        else:
                            break
            # print(height)
            # print(ret)
        return ret

