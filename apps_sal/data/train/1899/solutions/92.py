class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        found = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    found = True
                    break
            if found:
                break
        src = []
        q = []
        src.append((i, j))
        q.append((i, j))
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[i][j] = True
        while q:
            (curi, curj) = q.pop(0)
            for (nbori, nborj) in [(curi + 1, curj), (curi - 1, curj), (curi, curj + 1), (curi, curj - 1)]:
                if 0 <= nbori < m and 0 <= nborj < n:
                    if not visited[nbori][nborj] and A[nbori][nborj] == 1:
                        q.append((nbori, nborj))
                        visited[nbori][nborj] = True
                        src.append((nbori, nborj))
        found = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (not visited[i][j]):
                    found = True
                    break
            if found:
                break
        dest = []
        dest.append((i, j))
        q = []
        q.append((i, j))
        visited[i][j] = True
        while q:
            (curi, curj) = q.pop(0)
            for (nbori, nborj) in [(curi + 1, curj), (curi - 1, curj), (curi, curj + 1), (curi, curj - 1)]:
                if 0 <= nbori < m and 0 <= nborj < n:
                    if not visited[nbori][nborj] and A[nbori][nborj] == 1:
                        q.append((nbori, nborj))
                        visited[nbori][nborj] = True
                        dest.append((nbori, nborj))
        (source, target) = (src, dest)
        print(source, target)
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            (node, d) = queue.popleft()
            (curi, curj) = node
            if node in target:
                return d - 1
            for nei in [(curi + 1, curj), (curi - 1, curj), (curi, curj + 1), (curi, curj - 1)]:
                if nei not in done:
                    queue.append((nei, d + 1))
                    done.add(nei)
