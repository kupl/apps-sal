class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        move_pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        now_pos = move_pos[0]
        idx_now_pos = 0
        obstacles = set(map(tuple, obstacles))
        row_now = 0
        col_now = 0
        answer = 0
        for command in commands:
            if command > 0:
                for _ in range(command):
                    row_tmp = row_now + now_pos[0]
                    col_tmp = col_now + now_pos[1]
                    if (col_tmp, row_tmp) not in obstacles:
                        row_now += now_pos[0]
                        col_now += now_pos[1]
                        answer = max(answer, row_now ** 2 + col_now ** 2)
            else:
                if command == -1:
                    idx_now_pos += 1
                    if idx_now_pos > 3:
                        idx_now_pos = 0
                elif command == -2:
                    idx_now_pos -= 1
                    if idx_now_pos < 0:
                        idx_now_pos = 3
                now_pos = move_pos[idx_now_pos]
        return answer
