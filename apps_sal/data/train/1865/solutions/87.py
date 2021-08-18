class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'T':
                    target = (i, j)
                elif grid[i][j] == 'B':
                    start_box = (i, j)
                elif grid[i][j] == 'S':
                    start_person = (i, j)

        def heuristic(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])

        def out_bounds(location):
            i, j = location
            if i < 0 or i >= n:
                return True
            if j < 0 or j >= m:
                return True
            return grid[i][j] == '

        heap = [[heuristic(start_box), 0, start_person, start_box]]
        visited = set()

        while heap:
            _, moves, person, box = heapq.heappop(heap)
            if box == target:
                return moves
            if (person, box) in visited:
                continue
            visited.add((person, box))

            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_person = (person[0] + dx, person[1] + dy)
                if out_bounds(new_person):
                    continue

                if new_person == box:
                    new_box = (box[0] + dx, box[1] + dy)
                    if out_bounds(new_box):
                        continue
                    heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, new_person, new_box])
                else:
                    heapq.heappush(heap, [heuristic(box) + moves, moves, new_person, box])

        return -1
