from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        def at(point):
            (x, y) = point
            return grid[y][x]

        def valid(point):
            (x, y) = point
            return 0 <= y < len(grid) and 0 <= x < len(grid[y])

        def neighbors(point):
            (x, y) = point
            candidates = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
            for candidate in candidates:
                if valid(candidate):
                    yield candidate

        def moves(point, remaining):
            for neighbor in neighbors(point):
                if at(neighbor) == 1 and remaining > 0:
                    yield (neighbor, remaining - 1)
                elif at(neighbor) == 0:
                    yield (neighbor, remaining)
        start = ((0, 0), k)
        prev = {start: None}

        def path_length(node):
            length = 0
            while node:
                length += 1
                node = prev[node]
            return length
        frontier = deque([start])
        while frontier:
            (point, remaining) = frontier.popleft()
            (x, y) = point
            if y == len(grid) - 1 and x == len(grid[y]) - 1:
                return path_length((point, remaining)) - 1
            for move in moves(point, remaining):
                if move not in prev:
                    frontier.append(move)
                    prev[move] = (point, remaining)
        return -1
