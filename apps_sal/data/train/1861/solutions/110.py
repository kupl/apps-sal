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
    " mine\n    class Solution:\n    def minAreaRect(self, points: List[List[int]]) -> int:\n                \n        Y = dict()\n        X = dict()                \n        for point in points:\n            x, y = point[0], point[1]\n            if x not in X:\n                X[x] = set()\n            X[x].add(y)\n            \n            if y not in Y:\n                Y[y] = set()\n            Y[y].add(x)\n        \n                \n        _min = float('inf')\n        for point in points:            \n            x, y = point[0], point[1]\n            for _y in X[x]:\n                if _y > y:\n                    for _x in Y[_y]:\n                        if _x > x and _x in Y[y]:\n                            h = abs(_y - y)\n                            w = abs(_x - x)                    \n                            if h * w != 0:\n                                _min = min(_min, h * w)\n                        \n        if _min == float('inf'):\n            return 0\n        \n        return _min\n            \n    \n    "


"\n    def minAreaRect(self, points):\n        n = len(points)\n        nx = len(set(x for x, y in points))\n        ny = len(set(y for x, y in points))\n        if nx == n or ny == n:\n            return 0\n\n        p = collections.defaultdict(list)\n        if nx > ny:\n            for x, y in points:\n                p[x].append(y)\n        else:\n            for x, y in points:\n                p[y].append(x)\n\n        lastx = {}\n        res = float('inf')\n        for x in sorted(p):\n            p[x].sort()\n            for i in range(len(p[x])):\n                for j in range(i):\n                    y1, y2 = p[x][j], p[x][i]\n                    if (y1, y2) in lastx:\n                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))\n                    lastx[y1, y2] = x\n        return res if res < float('inf') else 0\n\n"
