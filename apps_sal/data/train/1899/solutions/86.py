class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])

        def getNeighbors(i, j):
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if x >= 0 and x < rows and y >= 0 and y < cols:
                    yield x, y

        def findComponents():
            visited = set()
            connectedNodes = [[] for i in range(2)]

            def findConnnectedComponent(i, j):
                visited.add((i, j))
                connectedNodes[connectedCompNumber].append((i, j))
                for x, y in getNeighbors(i, j):
                    if (x, y) not in visited and A[x][y]:
                        findConnnectedComponent(x, y)

            connectedCompNumber = -1
            for i in range(rows):
                for j in range(cols):
                    if (i, j) not in visited and A[i][j] == 1:
                        connectedCompNumber += 1
                        findConnnectedComponent(i, j)
            return connectedNodes

        def findDistance() -> int:
            shortedDist = 1
            source, target = findComponents()

            queue = collections.deque()
            for s in source:
                queue.appendleft((s, 0))
            done = set()
            for s in source:
                done.add(s)
            while queue:
                node, dist = queue.pop()
                if node in target:
                    return dist - 1
                for n in getNeighbors(*node):
                    if n not in done:
                        queue.appendleft((n, dist + 1))
                        done.add(n)

        return findDistance()
