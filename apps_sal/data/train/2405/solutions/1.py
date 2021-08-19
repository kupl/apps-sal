class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = [0, 0]
        deg_x = 0
        deg_y = 1
        obstacles = set(map(tuple, obstacles))
        ans = 0
        for walk in commands:
            if walk == -2:
                (deg_x, deg_y) = (-deg_y, deg_x)
            elif walk == -1:
                (deg_x, deg_y) = (deg_y, -deg_x)
            else:
                while walk > 0:
                    pos[0] += deg_x
                    pos[1] += deg_y
                    walk -= 1
                    if (pos[0], pos[1]) in obstacles:
                        pos[0] -= deg_x
                        pos[1] -= deg_y
                        break
                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        return ans
