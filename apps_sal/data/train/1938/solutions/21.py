class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        all_x, all_y = set(), set()
        for x1, y1, x2, y2 in rectangles:
            all_x.add(x1)
            all_x.add(x2)
            all_y.add(y1)
            all_y.add(y2)
        all_x = list(all_x)
        all_x.sort()
        all_y = list(all_y)
        all_y.sort()

        x_map = {val: i for i, val in enumerate(all_x)}
        y_map = {val: i for i, val in enumerate(all_y)}
        area = [[0 for _ in range(len(y_map))] for _ in range(len(x_map))]

        for x1, y1, x2, y2 in rectangles:
            for x in range(x_map[x1], x_map[x2]):
                for y in range(y_map[y1], y_map[y2]):
                    area[x][y] = 1

        ans = 0
        for x in range(len(x_map)):
            for y in range(len(y_map)):
                if area[x][y]:
                    ans += (all_x[x + 1] - all_x[x]) * (all_y[y + 1] - all_y[y])
                    if ans > 1000000007:
                        ans %= 1000000007
        return ans
