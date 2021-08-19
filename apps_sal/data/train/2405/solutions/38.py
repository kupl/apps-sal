class Solution:
    coordinates = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def robotSim(self, cmd: List[int], ob: List[List[int]]) -> int:
        obstruction = set((tuple(x) for x in ob))
        curr = 0
        x = 0
        y = 0
        res = 0
        for c in cmd:
            if c == -2:
                curr -= 1
                if curr < 0:
                    curr = 3
            elif c == -1:
                curr = (curr + 1) % 4
            else:
                while c > 0:
                    (x, y) = (x + self.coordinates[curr][0], y + self.coordinates[curr][1])
                    if (x, y) in obstruction:
                        x = x - self.coordinates[curr][0]
                        y = y - self.coordinates[curr][1]
                        break
                    c -= 1
            res = max(res, x * x + y * y)
        return res
