class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        ret = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                maxRight = len(mat[0])
                for h in range(i, len(mat)):
                    for w in range(j, maxRight):
                        if mat[h][w] == 1:
                            ret += 1
                        else:
                            maxRight = w
                            break
        return ret
