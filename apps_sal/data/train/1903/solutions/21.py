class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        e = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                e.append([i, j])

        def h(x):
            return abs(points[x[0]][0] - points[x[1]][0]) + abs(points[x[0]][1] - points[x[1]][1])
        e.sort(key=lambda x: h(x))

        #print([[points[x], points[y], h((x,y))] for x,y in e])

        n = len(points)
        v = set()
        s = 0
        c = []

        def find(x):
            nonlocal c
            for i, cc in enumerate(c):
                if x in cc:
                    return i

        for ee in e:
            x, y = ee
            if y not in v and x not in v:
                c.append([x, y])
                v.add(x)
                v.add(y)
                s += h(ee)
            elif x not in v:
                yi = find(y)
                c[yi].append(x)
                v.add(x)
                s += h(ee)
            elif y not in v:
                xi = find(x)
                c[xi].append(y)
                v.add(y)
                s += h(ee)
            else:
                xi = find(x)
                yi = find(y)
                if xi == yi:
                    continue
                s += h(ee)
                c[xi] += c[yi]
                del c[yi]
                if len(v) == n and len(c) == 1:
                    return s
        # print(v)
        return s
