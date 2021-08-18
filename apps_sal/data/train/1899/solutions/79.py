from typing import List
from queue import Queue


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        first_island, second_island = set(), set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def get_all(x, y, island):
            if (x, y) in island or A[y][x] == 0:
                return

            island.add((x, y))

            for dx, dy in directions:
                if 0 <= x + dx < len(A[0]) and 0 <= y + dy < len(A):
                    get_all(x + dx, y + dy, island)

        first_in = False
        for y in range(len(A)):
            for x in range(len(A[0])):
                if A[y][x] == 1:
                    if not first_in:
                        get_all(x, y, first_island)
                        first_in = True

                    elif (x, y) not in first_island:
                        get_all(x, y, second_island)
                        break

        visited = set()
        q = Queue()
        for x, y in first_island:
            q.put((x, y, 0))

        while not q.empty():
            x, y, depth = q.get()

            if (x, y) in second_island:
                return depth - 1

            for dx, dy in directions:
                X, Y = x + dx, y + dy
                if 0 <= X < len(A[0]) and 0 <= Y < len(A) and (X, Y) not in visited:
                    q.put((X, Y, depth + 1))
                    visited.add((X, Y))
