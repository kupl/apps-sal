class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        u = {(i, j): (i, j) for i in range(len(A)) for j in range(len(A[0])) if A[i][j]}
        def head(p):
            if u[p] == p:
                return p
            h = head(u[p])
            u[p] = h
            return h

        def union(p1, p2):
            u[head(p2)] = head(p1)

        for i, row in enumerate(A):
            for j, v in enumerate(row):
                if not v:
                    continue

                if i and A[i-1][j]:
                    union((i - 1, j), (i, j))
                if j and A[i][j-1]:
                    union((i, j - 1), (i, j))

        grps = {p1: set() for p1, p2 in list(u.items()) if p1 == p2}
        for p in list(u.keys()):
            grps[head(p)].add(p)

        grps = list(grps.values())

        s = 0
        layer, target = grps
        while layer:
            new_layer = []
            for x, y in layer:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= len(A) or ny < 0 or ny >= len(A[0]):
                        continue
                    if A[nx][ny] == 1 and (nx, ny) in target:
                        return s
                    if not A[nx][ny]:
                        new_layer.append((nx, ny))
                        A[nx][ny] = -1
            s += 1
            layer = new_layer

        return  # invalid, must be able to find s


