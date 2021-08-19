class Solution:

    def __init__(self):
        self.map = None
        (self.w, self.h) = (0, 0)

    def get_neighbors(self, r, c):
        nei = []
        for rc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= rc[0] < self.h and 0 <= rc[1] < self.w:
                nei.append(rc)
        return nei

    def find_island(self):
        done = set()
        islands = []
        for r in range(len(self.map)):
            for c in range(len(self.map[0])):
                if self.map[r][c] and (r, c) not in done:
                    stack = [(r, c)]
                    seen = {(r, c)}
                    while stack:
                        cell = stack.pop(0)
                        neighbors = self.get_neighbors(cell[0], cell[1])
                        for nei in neighbors:
                            if self.map[nei[0]][nei[1]] and nei not in seen:
                                stack.append(nei)
                                seen.add(nei)
                    islands.append(seen)
                    done |= seen
        return islands

    def shortestBridge(self, A: List[List[int]]) -> int:
        self.map = A
        (self.w, self.h) = (len(A), len(A[0]))
        (source, target) = self.find_island()
        queue = [(node, 0) for node in source]
        while queue:
            (node, d) = queue.pop(0)
            if node in target:
                return d - 1
            neighbors = self.get_neighbors(node[0], node[1])
            for nei in neighbors:
                if nei not in source:
                    queue.append((nei, d + 1))
                    source.add(nei)
