class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:

        def first():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] == 1:
                        return (i, j)

        def first_island(i, j):
            stack = [(i, j)]
            island = []
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while stack:
                (x, y) = stack.pop()
                A[x][y] = 2
                island.append((x, y, 0))
                for (dx, dy) in dirs:
                    (tx, ty) = (x + dx, y + dy)
                    if len(A) > tx >= 0 and len(A[0]) > ty >= 0 and (A[tx][ty] == 1):
                        stack.append((tx, ty))
            return island

        def bfs(queue):
            queue = collections.deque(queue)
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while queue:
                length = len(queue)
                for _ in range(length):
                    (x, y, level) = queue.popleft()
                    for (dx, dy) in dirs:
                        (tx, ty) = (x + dx, y + dy)
                        if len(A) > tx >= 0 and len(A[0]) > ty >= 0:
                            if A[tx][ty] == 1:
                                return level
                            elif not A[tx][ty]:
                                A[tx][ty] = -1
                                queue.append((tx, ty, level + 1))
        return bfs(first_island(*first()))
