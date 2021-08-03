class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 10:20am

        # DFS

        cur = [0, 0]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_direction = 0  # facing north
        max_distance = -1
        obstacles = {tuple(i) for i in obstacles}  # have to use this to avoid TLE
        for c in commands:
            if c > 0:
                while c > 0:
                    # move forward
                    cx, cy = cur
                    next_pos = [cx + directions[cur_direction][0], cy + directions[cur_direction][1]]
                    if (cx + directions[cur_direction][0], cy + directions[cur_direction][1]) in obstacles:
                        break  # stop moving, go to next command
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

#         x, y = 0, 0   #current position of robot
#         dx, dy = 0, 1   #direction of robot
#         obs = {tuple(i) for i in obstacles}   #create set of obstacles for faster access
#         maxdist = 0   #store max distance after each command

#         for step in commands:
#             if 0 < step < 10:
#                 for i in range(step):
#                     x, y = x+dx, y+dy   #take each step individually
#                     if (x,y) in obs:   #take one step back if on an obstacle
#                         x, y = x-dx, y-dy
#                         break
#             elif step == -2:   #change direction | move left
#                 dx, dy = -dy, dx
#             elif step == -1:   #change direction | move right
#                 dx, dy = dy, -dx

#             maxdist = max(maxdist, x**2 + y**2)

#         return maxdist
