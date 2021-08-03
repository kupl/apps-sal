class Solution:

    def d(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        f = [[x] for x in points]
        c = [float('inf') for x in points]
        g = [-1 for x in points]

        r = []

        while len(f) > 1:
            i = 0
            c = [float('inf') for x in f]

            while i < len(f):
                dx = -1
                j = 0
                while j < len(f):
                    if i != j:
                        for x in f[i]:
                            for y in f[j]:
                                val = self.d(x, y)
                                if val < c[i]:
                                    c[i] = val
                                    g[i] = i
                                    dx = j

                    j += 1
                if dx != -1:

                    r.append(c[i])
                    f[i] += f[dx]
                    del f[dx]
                    del c[dx]
                    del g[dx]

                    i -= 1

                i += 1

        return sum(r)
