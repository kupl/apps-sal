class Solution(object):
    def shortestBridge(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val == 1:
                        A[r][c] = 2
                        stack = [(r, c)]
                        #seen = {(r, c)}
                        seen = [(r, c)]
                        while stack:
                            node = stack.pop()
                            for x, y in neighbors(*node):
                                if A[x][y] == 1:
                                    A[x][y] = 2
                                    stack.append((x, y))
                                    #seen.add((x, y))
                                    seen.append((x, y))
                        components.append(seen)
            return components

        source, target = get_components()
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
