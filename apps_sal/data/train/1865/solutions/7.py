class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'T':
                    target = (r, c)
                if grid[r][c] == 'S':
                    start_person = (r, c)
                if grid[r][c] == 'B':
                    start_box = (r, c)

        def heuristic(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])

        def out_bounds(location):
            r, c = location
            return r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '

        heap = [[heuristic(start_box), 0, start_person, start_box]]
        vis = set()
        while heap:
            _, moves, person, box = heapq.heappop(heap)
            if box == target:
                return moves
            if (person, box) in vis:
                continue
            vis.add((person, box))

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_person = (person[0] + dr, person[1] + dc)
                if out_bounds(new_person):
                    continue

                if new_person == box:
                    new_box = (box[0] + dr, box[1] + dc)
                    if out_bounds(new_box):
                        continue
                    heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, new_person, new_box])
                else:
                    heapq.heappush(heap, [heuristic(box) + moves, moves, new_person, box])

        return -1
