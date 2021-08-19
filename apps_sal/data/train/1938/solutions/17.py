class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        N = len(rectangles)
        (Xvals, Yvals) = (set(), set())
        for (x1, y1, x2, y2) in rectangles:
            Xvals.add(x1)
            Xvals.add(x2)
            Yvals.add(y1)
            Yvals.add(y2)
        imapx = sorted(Xvals)
        imapy = sorted(Yvals)
        mapx = {x: i for (i, x) in enumerate(imapx)}
        mapy = {y: i for (i, y) in enumerate(imapy)}
        grid = [[0] * len(imapy) for _ in imapx]
        for (x1, y1, x2, y2) in rectangles:
            for x in range(mapx[x1], mapx[x2]):
                for y in range(mapy[y1], mapy[y2]):
                    grid[x][y] = 1
        ans = 0
        for (x, row) in enumerate(grid):
            for (y, val) in enumerate(row):
                if val:
                    ans += (imapx[x + 1] - imapx[x]) * (imapy[y + 1] - imapy[y])
        return ans % (10 ** 9 + 7)
