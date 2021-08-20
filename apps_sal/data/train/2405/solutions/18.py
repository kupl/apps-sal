class Solution:

    def robotSim(self, c: List[int], b: List[List[int]]) -> int:
        (x, y, d, b, M) = (0, 0, 0, set([tuple(i) for i in b]), 0)
        for i in c:
            if i < 0:
                d = (d + 2 * i + 3) % 4
            elif d in [1, 3]:
                for x in range(x, x + (i + 1) * (2 - d), 2 - d):
                    if (x + (2 - d), y) in b:
                        break
            else:
                for y in range(y, y + (i + 1) * (1 - d), 1 - d):
                    if (x, y + (1 - d)) in b:
                        break
            M = max(M, x ** 2 + y ** 2)
        return M
