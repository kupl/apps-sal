class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        rows = len(A)
        cols = len(A[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def edge_check(ro, co):
            r = []
            for y, x in directions:
                nr = ro + y
                nc = co + x
                if nr < rows and nr >= 0 and nc < cols and nc >= 0 and A[nr][nc] == 0:
                    return True

        edges_1 = set()
        found_1 = False
        edges_2 = set()
        for row in range(rows):
            for col in range(cols):
                if A[row][col] == 1:
                    A[row][col] = '
                    q = collections.deque([])
                    q.append((row, col))
                    while q:
                        r, c = q.popleft()
                        if not found_1 and edge_check(r, c):
                            edges_1.add((r, c))
                        else:
                            if edge_check(r, c):
                                edges_2.add((r, c))
                        for y, x in directions:
                            nr = r + y
                            nc = c + x
                            if nr < rows and nr >= 0 and nc < cols and nc >= 0 and A[nr][nc] == 1:
                                q.append((nr, nc))
                                A[nr][nc] = '

                    found_1 = True

        c1 = sorted(list(edges_1), key=lambda x: (x[0], x[1]))
        c2 = sorted(list(edges_2), key=lambda x: (x[0], x[1]))

        d = 0

        ds = []

        for x1, x2 in c1[:400]:
            for y1, y2 in c2[:400]:
                ds.append(abs(x1 - y1) + abs(x2 - y2) - 1)

        return min(ds)
