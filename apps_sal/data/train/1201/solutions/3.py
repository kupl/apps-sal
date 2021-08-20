from collections import deque


def traverse(l, h, w, i, j, p):
    c = 0
    queue = deque([(i, j)])
    visited = [[False for i in range(w)] for i in range(h)]
    visited[i][j] = True
    while queue:
        d = queue.popleft()
        (x, y) = (d[0], d[1])
        c += 1
        if x + 1 < h and l[x + 1][y] < p and (not visited[x + 1][y]):
            queue.append((x + 1, y))
            visited[x + 1][y] = True
        if x - 1 >= 0 and l[x - 1][y] < p and (not visited[x - 1][y]):
            queue.append((x - 1, y))
            visited[x - 1][y] = True
        if y + 1 < w and l[x][y + 1] < p and (not visited[x][y + 1]):
            queue.append((x, y + 1))
            visited[x][y + 1] = True
        if y - 1 > -1 and l[x][y - 1] < p and (not visited[x][y - 1]):
            queue.append((x, y - 1))
            visited[x][y - 1] = True
    return c


for i1 in range(int(input())):
    (h, w, q) = map(int, input().split())
    l = []
    for i in range(h):
        l1 = list(map(int, input().split()))
        l += [l1]
    for i in range(q):
        (i, j, p) = map(int, input().split())
        i -= 1
        j -= 1
        if l[i][j] >= p:
            print(0)
        else:
            b = traverse(l, h, w, i, j, p)
            print(b)
