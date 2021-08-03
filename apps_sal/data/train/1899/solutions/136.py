class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        q = collections.deque()

        def ExploreIslands(x, y):
            if not 0 <= x < len(A) or not 0 <= y < len(A[0]) or A[x][y] == -1:
                return
            if A[x][y] == 1:
                A[x][y] = -1
                ExploreIslands(x, y + 1)
                ExploreIslands(x, y - 1)
                ExploreIslands(x + 1, y)
                ExploreIslands(x - 1, y)
            else:
                q.appendleft((x, y, 1))

        def FindFirstIsland():
            for i, row in enumerate(A):
                for j, val in enumerate(row):
                    if val == 1:
                        ExploreIslands(i, j)
                        return

        FindFirstIsland()
        while True:
            x, y, distance = q.popleft()
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= new_x < len(A) and 0 <= new_y < len(A[0]):
                    if A[new_x][new_y] == 1:
                        return distance
                    elif A[new_x][new_y] == 0:
                        A[new_x][new_y] = -1
                        q.append((new_x, new_y, distance + 1))
