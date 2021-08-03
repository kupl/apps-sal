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
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                count[1] += 1
                r = num_right[(i, j)]
                d = num_below[(i, j)]
                # print('******************')
                # print('Index', i,j)
                # print('Counts', r,d)
                # print(count)
                curr = set()
                if r == 0 and d == 0:
                    continue
                flag = True
                for k in range(2, min(r, d) + 2):
                    #print('Checking k=',k)
                    for x in range(i, i + k):
                        for y in range(j, j + k):
                            curr.add(matrix[x][y])
                            if matrix[x][y] == 0:
                                flag = False
                            if not flag:
                                break
                        if not flag:
                            break
                    if 0 not in curr and flag:
                        count[k] += 1
                    else:
                        break
        print(count)
        return sum(count.values())
