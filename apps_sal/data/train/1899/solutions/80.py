from queue import Queue


def valid(m, i, j):
    return 0 <= i < len(m) and 0 <= j < len(m[0])


def findAnIsland(m, e):
    stack = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1 and (i, j) not in e:
                stack.append((i, j))
                break
        else:
            continue
        break
    result, edges = set(), set()
    while stack:
        ci, cj = stack.pop()
        result.add((ci, cj))
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            cdi, cdj = ci + di, cj + dj
            if valid(m, cdi, cdj) and (cdi, cdj) not in e and (cdi, cdj) not in result:
                if m[cdi][cdj] == 1:
                    stack.append((cdi, cdj))
                else:
                    edges.add((ci, cj))
    return result, edges


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        a, aedges = findAnIsland(A, set())
        b, bedges = findAnIsland(A, a)
        min_flip, q = float('inf'), Queue()
        for i, j in aedges:
            q.put((i, j, 0))
        while not q.empty():
            ci, cj, dist = q.get()
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                cdi, cdj = ci + di, cj + dj
                if valid(A, cdi, cdj):
                    if (cdi, cdj) in bedges:
                        min_flip = min(min_flip, dist)
                    elif A[cdi][cdj] == 0 or A[cdi][cdj] > dist + 1:
                        A[cdi][cdj] = dist + 1
                        q.put((cdi, cdj, dist + 1))
        return min_flip
