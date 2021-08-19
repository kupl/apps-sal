class Solution:

    def numSubmat(self, mat) -> int:
        (m, n) = (len(mat), len(mat[0]))
        consective = [0] * m
        res = 0
        for line in range(n):
            for row in range(m):
                if mat[row][line] == 1:
                    consective[row] += 1
                else:
                    consective[row] = 0
            stack = []
            for i in range(m):
                val = consective[i]
                while stack and val <= stack[-1][0]:
                    stack.pop()
                stack.append((val, i))
                for k in range(len(stack)):
                    if k == 0:
                        (a, b) = stack[k]
                        res += a * (b + 1)
                    else:
                        (a, b) = stack[k - 1]
                        (c, d) = stack[k]
                        res += c * (d - b)
        return res
