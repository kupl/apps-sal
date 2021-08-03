class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A) if A else 0, len(A[0]) if A else 0
        p, q = -1, -1

        def neighbors(r, c):
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr in range(m) and nc in range(n):
                    yield nr, nc

        done = set()
        components = []

        for i, j in product(list(range(m)), list(range(n))):
            if A[i][j] == 1:
                # use dfs to detect the two island components
                if (i, j) not in done:
                    stack = [(i, j)]
                    seen = {(i, j)}
                    while stack:
                        node = stack.pop()
                        for p, q in neighbors(*node):
                            if (p, q) not in seen:
                                if A[p][q] == 1:
                                    seen.add((p, q))
                                    stack.append((p, q))
                    done |= seen
                    components.append(seen)

        source, target = components

        #
        # BFS lke search from all source cells to any target cell
        #
        heap = []
        for i, j in source:
            heappush(heap, (0, (i, j)))

        done = set(source)
        while heap:
            dist, (i, j) = heappop(heap)
            if (i, j) in target:
                return dist - 1
            for r, s in neighbors(i, j):
                if A[r][s] not in source and (r, s) not in done:
                    done.add((r, s))
                    heappush(heap, (dist + 1, (r, s)))
