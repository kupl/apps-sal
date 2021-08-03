class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:

        minn = len(A) * 2
        visited = [[False for _ in range(len(A))] for _ in range(len(A))]
        label = 1
        found = False

        islands = {1: [], 2: []}

        def dfs(i, j):
            nonlocal A, visited, label, found

            if i < 0 or j < 0 or i + 1 > len(A) or j + 1 > len(A) or visited[i][j]:
                return

            visited[i][j] = True

            if A[i][j] == 0:
                return

            islands[label].append((i, j))

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

            found = True

        for i in range(len(A)):
            for j in range(len(A)):
                if not visited[i][j]:
                    dfs(i, j)
                    if found:
                        label = 2

        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        source, target = islands[1], islands[2]
        print((source, target))
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target:
                return d - 1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d + 1))
                    done.add(nei)
