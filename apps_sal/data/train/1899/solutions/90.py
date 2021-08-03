class Solution:
    def __init__(self):
        self.components = []
        self.comp = []
        self.seen = set()

    def isValid(self, r, c, A):
        if r < 0 or c < 0 or r >= len(A) or c >= len(A):
            return False
        return True

    def dfs(self, r, c, A):
        if not self.isValid(r, c, A) or (r, c) in self.seen or A[r][c] != 1:
            return
        self.comp.append((r, c))
        self.seen.add((r, c))
        self.dfs(r + 1, c, A)
        self.dfs(r - 1, c, A)
        self.dfs(r, c + 1, A)
        self.dfs(r, c - 1, A)

    def shortestBridge(self, A: List[List[int]]) -> int:

        for i in range(len(A)):
            for j in range(len(A[0])):
                if (i, j) not in self.seen and A[i][j] == 1:
                    self.comp = []
                    self.dfs(i, j, A)
                    self.components.append(self.comp)

        source, target = self.components
        visited = set(source)
        queue = collections.deque([(node, 0) for node in source])

        while queue:
            node, d = queue.popleft()
            if node in target:
                return d - 1
            else:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = node[0] + dr
                    nc = node[1] + dc
                    if (nr, nc) not in visited and self.isValid(nr, nc, A):
                        queue.append(((nr, nc), d + 1))
                        visited.add((nr, nc))
        return -1
