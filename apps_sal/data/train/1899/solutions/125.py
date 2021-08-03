class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        starting_points = set()

        def traverse_island(r, c):
            A[r][c] = -1

            for ar, ac in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= ar < rows and 0 <= ac < cols:
                    if A[ar][ac] == 0:
                        starting_points.add((ar, ac, 0))
                    elif A[ar][ac] == 1:
                        traverse_island(ar, ac)

        for r in range(rows):
            for c in range(cols):
                if A[r][c] == 1:
                    traverse_island(r, c)
                    break
            else:
                continue

            break

        q = deque(starting_points)

        while q:
            r, c, dist = q.popleft()

            for ar, ac in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= ar < rows and 0 <= ac < cols and A[ar][ac] != -1:
                    if A[ar][ac] == 1:
                        return dist + 1

                    A[ar][ac] = -1
                    q.append((ar, ac, dist + 1))

        return 0
