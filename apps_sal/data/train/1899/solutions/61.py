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

        minn = float('inf')

        for x1, x2 in edges_1:
            for y1, y2 in edges_2:
                minn = min(minn, abs(x1 - y1) + abs(x2 - y2) - 1)

        return minn
