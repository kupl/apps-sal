class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def helper(x, y):
            temp = 0
            pre = [[x, y]]
            side = 1
            while True:
                flag = 1
                nxt = []
                for i in range(len(pre)):
                    a, b = pre[i]
                    if a + 1 >= len(matrix) or b + 1 >= len(matrix[0]) or matrix[a + 1][b + 1] != 1 or matrix[a + 1][b] != 1 or matrix[a][b + 1] != 1:
                        flag = 0
                        break
                    if i - side == -1:
                        nxt.append([a, b + 1])
                        nxt.append([a + 1, b + 1])
                        nxt.append([a + 1, b])
                    elif i - side >= 0:
                        nxt.append([a + 1, b])
                    else:
                        nxt.append([a, b + 1])
                if flag == 0:
                    break
                temp += 1
                side += 1
                pre = nxt
            return temp
            
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                res += 1
                res += helper(i, j)
        return res
