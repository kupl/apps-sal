class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        answer = []
        temp = []
        (val, i, j) = (0, 0, 0)
        for r in range(max(0, i - K), min(i + K + 1, m)):
            for c in range(max(0, j - K), min(j + K + 1, n)):
                val += mat[r][c]
        temp.append(val)
        for i in range(m):
            if i == 0:
                row = temp
            else:
                row = []
                r1 = i - K - 1
                r2 = i + K
                (subs2, adds2) = (0, 0)
                for c in range(max(0, -K), min(K + 1, n)):
                    if r1 >= 0:
                        subs2 += mat[r1][c]
                    if r2 < m:
                        adds2 += mat[r2][c]
                row.append(answer[-1][0] + adds2 - subs2)
            for j in range(1, n):
                (subs, adds) = (0, 0)
                c1 = j - K - 1
                c2 = j + K
                for r in range(max(0, i - K), min(i + K + 1, m)):
                    if c1 >= 0:
                        subs += mat[r][c1]
                    if c2 < n:
                        adds += mat[r][c2]
                row.append(row[-1] + adds - subs)
            answer.append(row)
        return answer
