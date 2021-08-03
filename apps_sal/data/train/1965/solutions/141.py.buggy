
class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        \"\"\"
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        \"\"\"

        ga = [i for i in range(n)]
        gb = [i for i in range(n)]

        res = 0

        e1 = []
        e2 = []
        for i in range(len(edges)):
            if edges[i][0] == 1:
                e1.append(edges[i])
                continue
            if edges[i][0] == 2:
                e2.append(edges[i])
                continue

            x = edges[i][1]-1
            y = edges[i][2]-1

            gx = self.get_group(ga, x)
            gy = self.get_group(ga, y)
            if gx == gy:
                res += 1
            ga[gx] = min(gx, gy)
            ga[gy] = min(gx, gy)
            ga[x] = min(gx, gy)
            ga[y] = min(gx, gy)
            gb[gx] = min(gx, gy)
            gb[gy] = min(gx, gy)
            gb[x] = min(gx, gy)
            gb[y] = min(gx, gy)

        for e in e1:
            x = e[1]-1
            y = e[2]-1
            gx = self.get_group(ga, x)
            gy = self.get_group(ga, y)
            if gx == gy:
                res += 1
            ga[gx] = min(gx, gy)
            ga[gy] = min(gx, gy)
            ga[x] = min(gx, gy)
            ga[y] = min(gx, gy)

        for e in e2:
            x = e[1]-1
            y = e[2]-1
            gx = self.get_group(gb, x)
            gy = self.get_group(gb, y)
            if gx == gy:
                res += 1
            gb[gx] = min(gx, gy)
            gb[gy] = min(gx, gy)
            gb[x] = min(gx, gy)
            gb[y] = min(gx, gy)

        ga0 = self.get_group(ga, 0)
        gb0 = self.get_group(gb, 0)
        for i in range(1, n):
            gai = self.get_group(ga, i)
            gbi = self.get_group(gb, i)
            if ga0 != gai or gb0 != gbi:
                return -1
        return res

    def get_group(self, g, i):

        gi = g[i]
        pre = i
        while gi != g[gi]:
            g[pre] = g[gi]
            pre = gi
            gi = g[gi]

        return gi
