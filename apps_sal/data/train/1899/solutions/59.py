class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        R, C = len(A), len(A[0])

        def getNeighbors(curr_points):
            neighbors = set()
            for i, j in curr_points:

                for row, col in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:

                    if 0 <= row < R and 0 <= col < C:
                        neighbors.add((row, col))

            return neighbors

        def get_islands():
            def dfs(pos, visited):
                i, j = pos

                if (i >= R or
                    i < 0 or
                    j >= C or
                    j < 0 or
                    A[i][j] == 0 or
                        pos in visited):
                    return

                visited.add(pos)

                dfs((i + 1, j), visited)
                dfs((i - 1, j), visited)
                dfs((i, j + 1), visited)
                dfs((i, j - 1), visited)

            island1, island2 = set(), set()

            for i in range(R):
                for j in range(C):

                    if A[i][j] == 1:
                        if not island1:
                            dfs((i, j), island1)
                        elif not island2 and (i, j) not in island1:
                            dfs((i, j), island2)

            return island1, island2

        island1, island2 = get_islands()

        min_distance = 0

        while True:
            neighbors = getNeighbors(island1)
            for neighbor in neighbors:
                if neighbor in island2:
                    return min_distance

                island1.add(neighbor)
            min_distance += 1

        return min_distance

    def dist(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1]) - 1
