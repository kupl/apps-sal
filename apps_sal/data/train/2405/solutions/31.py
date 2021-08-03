class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        x, y = (0, 0)

        ob = set([tuple(i) for i in obstacles])

        dd = {0: [[-1, 0]], 1: [[0, 1]], 2: [[1, 0]], 3: [[0, -1]]}

        d = 1

        ans = 0

        for i in commands:
            if i < 0:
                d += 1 if i == -1 else -1
                d %= 4
            else:
                for m, n in dd[d]:
                    while i and (x + m, y + n) not in ob:
                        x += m
                        y += n
                        i -= 1
                    ans = max(ans, x**2 + y**2)

        return ans
