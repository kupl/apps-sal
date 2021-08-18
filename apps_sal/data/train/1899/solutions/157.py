from collections import deque


class Solution:
    def findNeighbors(self, root, A):
        i, j = root
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if i < len(A) - 1:
            neighbors.append((i + 1, j))
        if j < len(A[0]) - 1:
            neighbors.append((i, j + 1))
        return neighbors

    def findIsland(self, root, A):
        queue = [root]
        visited = set()
        while queue:
            pick = queue.pop()
            if pick in visited:
                continue
            visited.add(pick)

            neighbors = self.findNeighbors(pick, A)
            for neighbor in neighbors:
                if A[neighbor[0]][neighbor[1]] == 1:
                    queue.append(neighbor)
        return visited

    def shortestBridge(self, A: List[List[int]]) -> int:
        root = None
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    root = (i, j)

        queue = deque(self.findIsland(root, A))
        level = 0
        visited = self.findIsland(root, A)
        while queue:
            print((level, queue, visited))
            for _ in range(len(queue)):
                pick = queue.popleft()
                for neighbor in self.findNeighbors(pick, A):
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    if A[neighbor[0]][neighbor[1]] == 1:
                        print(neighbor)
                        return level
                    queue.append(neighbor)
            level += 1

        return level
