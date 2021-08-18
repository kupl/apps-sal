from sys import stdin, stdout
import sys
from bisect import bisect_left, bisect_right


t = int(stdin.readline().strip())

for _ in range(t):
    n, m = stdin.readline().strip().split(' ')
    n, m = int(n), int(m)
    arr = []
    for i in range(n):
        arr.append(list(map(int, stdin.readline().strip().split(' '))))
    ctr = 0
    visited = [[False for i in range(m)] for j in range(n)]
    sol = [[1 for i in range(m)] for j in range(n)]
    pq = []
    for i in range(n):
        for j in range(m):
            pq.append((arr[i][j], i, j))
    pq = sorted(pq, key=lambda e: (e[0]), reverse=True)
    for i in pq:
        cv, yo, xo = i
        if visited[yo][xo]:
            continue
        else:
            stack = [xo, yo]
            while len(stack):
                y = stack.pop(-1)
                x = stack.pop(-1)
                visited[y][x] = True
                ctr += 1
                sol[y][x] = 0
                if x - 1 >= 0 and x - 1 < m and y + 1 >= 0 and y + 1 < n:
                    if not visited[y + 1][x - 1]:
                        stack.append(x - 1)
                        stack.append(y + 1)
                if x >= 0 and x < m and y + 1 >= 0 and y + 1 < n:
                    if not visited[y + 1][x]:
                        stack.append(x)
                        stack.append(y + 1)
                if x + 1 >= 0 and x + 1 < m and y + 1 >= 0 and y + 1 < n:
                    if not visited[y + 1][x + 1]:
                        stack.append(x + 1)
                        stack.append(y + 1)
            sol[yo][xo] = 1

    for i in sol:
        for j in i:
            stdout.write(str(j))
        stdout.write("\n")
