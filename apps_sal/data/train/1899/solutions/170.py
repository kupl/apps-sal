class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        m = len(A)
        n = len(A[0])

        def get_neighbors(i, j):
            dirs = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),

            ]

            ans = []

            for dx, dy in dirs:
                new_i = i + dx
                new_j = j + dy

                if 0 <= new_i < m and 0 <= new_j < n:
                    ans.append((new_i, new_j))

            return ans

        def dfs_visit(i, j, visited):

            if A[i][j] != 1:
                return

            if (i, j) in visited:
                return

            visited.add((i, j))

            for neighbor in get_neighbors(i, j):
                dfs_visit(neighbor[0], neighbor[1], visited)

            return

        source_nodes = set()
        break_flag = False

        for i in range(m):

            if break_flag:
                break
            for j in range(n):
                # print(i, j)

                if A[i][j] == 1:
                    dfs_visit(i, j, source_nodes)
                    break_flag = True
                    break

        q = []
        for i, j in source_nodes:
            q.append(((i, j), 0))

        visited = set()

        # print(q)

        while len(q):
            curr_node, curr_dist = q.pop(0)

            for neighbor in get_neighbors(curr_node[0], curr_node[1]):
                if neighbor in source_nodes:
                    continue

                if neighbor in visited:
                    continue

                if A[neighbor[0]][neighbor[1]] == 1:
                    return curr_dist

                visited.add(neighbor)
                q.append((neighbor, curr_dist + 1))

        return
