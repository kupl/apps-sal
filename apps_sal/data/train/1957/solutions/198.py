class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        job_list = deque()

        def def_value():
            return []
        graph = defaultdict(def_value)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inBounds(i, j):
            return 0 <= i and i < m and 0 <= j and j < n

        for i in range(m):
            for j in range(n):
                for dir_pair in dirs:
                    next_point_i = i + dir_pair[0]
                    next_point_j = j + dir_pair[1]
                    if inBounds(next_point_i, next_point_j):
                        if grid[next_point_i][next_point_j] == 1:
                            graph[(i, j)].append((next_point_i, next_point_j, 1))
                        else:
                            graph[(i, j)].append((next_point_i, next_point_j, 0))

        job_list.append((0, 0, k, 0))
        visited_set = set()
        # print(graph)
        while len(job_list) > 0:
            cur = job_list.popleft()
            if cur[0] == m - 1 and cur[1] == n - 1:
                return cur[3]
            if (cur[0], cur[1], cur[2]) not in visited_set:
                visited_set.add((cur[0], cur[1], cur[2]))
            else:
                continue

            neighbors = graph[(cur[0], cur[1])]
            for neighbor in neighbors:
                if neighbor[2] == 1:
                    if cur[2] > 0:
                        job_list.append((neighbor[0], neighbor[1], cur[2] - 1, cur[3] + 1))
                else:
                    job_list.append((neighbor[0], neighbor[1], cur[2], cur[3] + 1))
        if (m - 1, n - 1) not in visited_set:
            return -1
        else:
            return visited_set[(m - 1, n - 1)]
