class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        ans = 0
        topleft = [0 for i in matrix[0]]
        totop = [0 for i in matrix[0]]
        for i in range(len(matrix)):
            toleft, nextarea = 0, [0 for i in range(len(matrix[0])+1)]
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    totop[j] += 1
                    toleft += 1
                    maxr = min(totop[j], toleft, topleft[j] + 1)
                    nextarea[j + 1] = maxr
                    ans += maxr
                else:
                    totop[j] = 0
                    toleft = 0
                    nextarea[j + 1] = 0
            topleft = nextarea
        return ans
