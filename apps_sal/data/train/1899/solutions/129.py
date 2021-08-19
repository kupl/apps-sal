class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        (R, C) = (len(A), len(A[0]))

        def neighbors(r, c):
            for (nr, nc) in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield (nr, nc)

        def get_components():
            done = set()
            components = []
            for (r, row) in enumerate(A):
                for (c, val) in enumerate(row):
                    if val and (r, c) not in done:
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for (dr, dc) in neighbors(*node):
                                if A[dr][dc] and (dr, dc) not in seen:
                                    stack.append((dr, dc))
                                    seen.add((dr, dc))
                        done |= seen
                        components.append(seen)
            return components
        (source, target) = get_components()
        print((source, target))
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            (node, d) = queue.popleft()
            if node in target:
                return d - 1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d + 1))
                    done.add(nei)
