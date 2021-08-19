class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di = 0
        cur = [0, 0]
        obs = set([tuple(x) for x in obstacles])
        maxx = 0
        for i in commands:
            if i == -2:
                di = di - 1 if di > 0 else 3
            elif i == -1:
                di = (di + 1) % 4
            else:
                for x in range(i):
                    (xi, yi) = (cur[0] + d[di][0], cur[1] + d[di][1])
                    if (xi, yi) in obs:
                        break
                    cur = (xi, yi)
                    maxx = max(maxx, cur[0] ** 2 + cur[1] ** 2)
        return maxx
