from collections import defaultdict


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        num_right = defaultdict(lambda: 0)
        num_below = defaultdict(lambda: 0)
        m = len(matrix)
        n = len(matrix[0])

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if j + 1 < n:
                    num_right[(i, j)] = num_right[(i, j + 1)] + 1 if matrix[i][j + 1] == 1 else num_right[(i, j + 1)]
                else:
                    num_right[(i, j)] = 0
                if i + 1 < m:
                    num_below[(i, j)] = num_below[(i + 1, j)] + 1 if matrix[i + 1][j] == 1 else num_below[(i + 1, j)]
                else:
                    num_below[(i, j)] = 0

        count = defaultdict(lambda: 0)
        partial = defaultdict(lambda: 0)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if matrix[i][j] == 0:
                    continue
                r = num_right[(i, j)]
                d = num_below[(i, j)]
                # print('******************')
                # print('Index', i,j)
                # print('Counts', r,d)
                # print(count)
                # print(partial)
                if matrix[i][j] == 1:
                    partial[(i, j, 1)] = 1
                    count[1] += 1
                diff = min(r, d)
                flag = True
                for k in range(2, diff + 2):
                    #print('Checking k=', k)
                    if partial[(i, j + 1, k - 1)] == 1 and partial[(i + 1, j + 1, k - 1)] == 1 and partial[(i + 1, j, k - 1)] == 1:
                        partial[(i, j, k)] = 1
                        count[k] += 1
                    else:
                        flag = False
                    if not flag:
                        break

        # print(count)
        return sum(count.values())
