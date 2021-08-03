class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        free = set((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell != '#')
        target = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'T')
        boxi, boxj = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'B')
        si, sj = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'S')
        heap = [(0, si, sj, boxi, boxj)]

        def add(moves, *state, added=set()):
            if state not in added:
                heapq.heappush(heap, (moves, *state))
                added.add(state)
        while heap:
            moves, si, sj, boxi, boxj = heapq.heappop(heap)
            if (boxi, boxj) == target:
                return moves
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                ni, nj = si + dx, dy + sj
                if (ni, nj) == (boxi, boxj):
                    if (boxi + dx, boxj + dy) in free:
                        add(moves + 1, ni, nj, boxi + dx, boxj + dy)
                elif (ni, nj) in free:
                    add(moves, ni, nj, boxi, boxj)
        return -1
