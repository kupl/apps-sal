class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # https://leetcode.com/problems/shortest-bridge/discuss/843901/Python-Easy-BFS-Approach-with-Comments!
        rows = len(A)
        cols = len(A[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        # Function to check if a given location is an edge.
        def edge_check(ro, co):
            r = []
            for y, x in directions:
                nr = ro + y
                nc = co + x
                if nr < rows and nr >= 0 and nc < cols and nc >= 0 and A[nr][nc] == 0:
                    return True
            return False
        # Keep a flag for when we finish surveying the 1st island.
        edges_1 = set()
        found_1 = False
        edges_2 = set()
        # Work through our grid until we find an island.
        for row in range(rows):
            for col in range(cols):
                # If we find one we'll start our bfs, marking visited locations with # so we don't revisit.
                if A[row][col] == 1:
                    A[row][col] = '#'
                    q = collections.deque([])
                    q.append((row, col))
                    while q:
                        r, c = q.popleft()
                        # If we haven't found 1 yet (we must be working through 1 now).
                        # Append the edge (row, col).
                        if not found_1 and edge_check(r, c):
                            edges_1.add((r, c))
                        # Otherwise we must be on island 2.
                        else:
                            if edge_check(r, c):
                                edges_2.add((r, c))
                        # Continue working through the adjacent cells.
                        for y, x in directions:
                            nr = r + y
                            nc = c + x
                            if nr < rows and nr >= 0 and nc < cols and nc >= 0 and A[nr][nc] == 1:
                                q.append((nr, nc))
                                A[nr][nc] = '#'

                    found_1 = True
        # Sort the coordinates
        c1 = sorted(list(edges_1), key=lambda x: (x[0], x[1]))
        c2 = sorted(list(edges_2), key=lambda x: (x[0], x[1]))

        minn = float('inf')
        # Find/return the min distance between points.
        for x1, x2 in c1[:250]:
            for y1, y2 in c2[:250]:
                minn = min(minn, abs(x1-y1)+abs(x2-y2)-1)

        return minn
