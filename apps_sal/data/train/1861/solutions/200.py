class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        res = float('inf')
        for point in points:
            (x, y) = (point[0], point[1])
            for (_x, _y) in seen:
                if (x, _y) in seen and (_x, y) in seen:
                    res = min(res, abs(x - _x) * abs(y - _y))
            seen.add((x, y))
        if res == float('inf'):
            return 0
        return res


"\n    def minAreaRect(self, points):\n        n = len(points)\n        nx = len(set(x for x, y in points))\n        ny = len(set(y for x, y in points))\n        if nx == n or ny == n:\n            return 0\n\n        p = collections.defaultdict(list)\n        if nx > ny:\n            for x, y in points:\n                p[x].append(y)\n        else:\n            for x, y in points:\n                p[y].append(x)\n\n        lastx = {}\n        res = float('inf')\n        for x in sorted(p):\n            p[x].sort()\n            for i in range(len(p[x])):\n                for j in range(i):\n                    y1, y2 = p[x][j], p[x][i]\n                    if (y1, y2) in lastx:\n                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))\n                    lastx[y1, y2] = x\n        return res if res < float('inf') else 0\n\n"
