class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] in ['#', '.']:
                    continue
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                else:
                    target = (i, j)

        def heuristic(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])

        @functools.lru_cache(None)
        def reach(player, pos, box):
            i, j = pos
            if not (0 <= i < M and 0 <= j < N and grid[i][j] != '#'):
                return False
            hp = [player]
            seen = set([player])
            while hp:
                player = heapq.heappop(hp)
                if player == pos:
                    return True
                p0, p1 = player
                for i, j in [(p0 - 1, p1), (p0 + 1, p1), (p0, p1 - 1), (p0, p1 + 1)]:
                    if 0 <= i < M and 0 <= j < N and grid[i][j] != '#' and (i, j) != box and (i, j) not in seen:
                        seen.add((i, j))
                        heapq.heappush(hp, (i, j))
            return False

        seen = set([(box, player)])
        hp = [(heuristic(box), 0, box, player)]
        while hp:
            _, step, box, player = heapq.heappop(hp)
            print(box)
            if box == target:
                return step
            b0, b1 = box
            for i, j in [(b0 - 1, b1), (b0 + 1, b1), (b0, b1 - 1), (b0, b1 + 1)]:
                if 0 <= i < M and 0 <= j < N and grid[i][j] != '#' and ((i, j), player) not in seen and reach(player, (
                        b0 * 2 - i, b1 * 2 - j), box):
                    seen.add(((i, j), player))
                    heapq.heappush(hp, (heuristic((i, j)) + step + 1, step + 1, (i, j), box))
        return -1
