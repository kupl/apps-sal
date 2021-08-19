class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        cur = [0, 0]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_direction = 0
        max_distance = -1
        obstacles = {tuple(i) for i in obstacles}
        for c in commands:
            if c > 0:
                while c > 0:
                    (cx, cy) = cur
                    next_pos = [cx + directions[cur_direction][0], cy + directions[cur_direction][1]]
                    if (cx + directions[cur_direction][0], cy + directions[cur_direction][1]) in obstacles:
                        break
                    cur = next_pos
                    c -= 1
            elif c == -1:
                cur_direction += 1
                if cur_direction > 3:
                    cur_direction = 0
            elif c == -2:
                cur_direction -= 1
                if cur_direction < 0:
                    cur_direction = 3
            max_distance = max(max_distance, cur[0] * cur[0] + cur[1] * cur[1])
        return max_distance
