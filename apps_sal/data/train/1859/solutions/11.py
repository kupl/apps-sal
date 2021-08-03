class Solution:
    def countSquares(self, a: List[List[int]]) -> int:
        d = []
        r = len(a) + 1
        c = len(a[0]) + 1
        d = [[0 for j in range(c)] for i in range(r)]
        for i in range(1, r):
            for j in range(1, c):
                if(a[i - 1][j - 1] == 1):
                    d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])
        print(d)
        return sum(map(sum, d))
