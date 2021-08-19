class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        # two source bfs

        def neighbor(r, c):
            for nr, nc in [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                    yield nr, nc

        def can_reach(worker, target, box):
            if worker == target:
                return True
            if target[0] >= R or target[0] < 0 or target[1] >= C or target[1] < 0 or grid[target[0]][target[1]] == '#':
                return False

            start = [worker]
            end = [target]
            start_seen = {worker}
            end_seen = {target}

            while start and end:
                n_start = []
                for node in start:
                    r, c = node
                    for nr, nc in neighbor(r, c):
                        if (nr, nc) in end_seen:
                            return True
                        if (nr, nc) != box and (nr, nc) not in start_seen:
                            start_seen.add((nr, nc))
                            n_start.append((nr, nc))
                n_end = []
                for node in end:
                    r, c = node
                    for nr, nc in neighbor(r, c):
                        if (nr, nc) in start_seen:
                            return True
                        if (nr, nc) != box and (nr, nc) not in end_seen:
                            end_seen.add((nr, nc))
                            n_end.append((nr, nc))
                start = n_start
                end = n_end

        S, B, T = None, None, None

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'S':
                    S = (r, c)
                elif grid[r][c] == 'B':
                    B = (r, c)
                elif grid[r][c] == 'T':
                    T = (r, c)

        level = [(S, B)]
        seen = {(S, B)}
        steps = 0
        while level:
            n_level = []
            for player, box in level:
                r, c = box
                for nr, nc in neighbor(r, c):
                    opp_r, opp_c = 2 * r - nr, 2 * c - nc
                    if can_reach(player, (opp_r, opp_c), box):
                        if (nr, nc) == T:
                            return steps + 1
                        n_state = (box, (nr, nc))
                        if n_state not in seen:
                            seen.add(n_state)
                            n_level.append(n_state)

            level = n_level
            # print(seen, level)
            steps += 1
        return -1
