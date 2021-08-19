class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        y2x = collections.defaultdict(list)
        for (x, y) in points:
            y2x[y].append(x)
        res = float('inf')
        ys = list(y2x.keys())
        for y1 in ys:
            for y2 in ys:
                if y1 != y2:
                    x1List = y2x[y1]
                    x2Set = y2x[y2]
                    canList = []
                    for x1 in x1List:
                        if x1 in x2Set:
                            canList.append(x1)
                    for m in canList:
                        for n in canList:
                            if m != n:
                                res = min(res, abs(m - n) * abs(y1 - y2))
        if res == float('inf'):
            return 0
        return res
