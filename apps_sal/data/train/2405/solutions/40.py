class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        cur_pos = (0, 0)
        d = 0
        m = 0

        cur_steps = 0
        for cmd_idx, cmd in enumerate(commands):
            if cmd < 0:
                cur_pos = self.new_pos(obs, d, cur_steps, cur_pos)
                m = max(m, cur_pos[0] ** 2 + cur_pos[1] ** 2)
                cur_steps = 0

                if cmd == -2:
                    d = (d - 1) % 4
                elif cmd == -1:
                    d = (d + 1) % 4
            else:
                cur_steps += cmd

        cur_pos = self.new_pos(obs, d, cur_steps, cur_pos)
        m = max(m, cur_pos[0] ** 2 + cur_pos[1] ** 2)
        return m

    def new_pos(self, obs, d, cur_steps, cur_pos):
        if cur_steps == 0:
            return cur_pos

        if d == 0:
            idx = 1
            incr = 1
        elif d == 1:
            idx = 0
            incr = 1
        elif d == 2:
            idx = 1
            incr = -1
        elif d == 3:
            idx = 0
            incr = -1

        while cur_steps > 0:
            if idx == 0:
                next_pos = (cur_pos[0] + incr, cur_pos[1])
            else:
                next_pos = (cur_pos[0], cur_pos[1] + incr)
            if next_pos in obs:
                break
            cur_pos = next_pos
            cur_steps -= 1
        return cur_pos
