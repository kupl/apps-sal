class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        x_lines, y_lines = {}, {}
        for x, y in points:
            x_lines[x] = x_lines.get(x, set()) | {y}
            y_lines[y] = y_lines.get(y, set()) | {x}
        # print(x_lines, y_lines)
        res = float('inf')
        for x, y_s in x_lines.items():
            if len(y_s) < 2:
                continue
            # print(x, y_s)
            y_s = list(y_s)
            for i in range(len(y_s)):
                for j in range(i + 1, len(y_s)):
                    y1, y2 = y_s[i], y_s[j]
                    inter = y_lines[y1].intersection(y_lines[y2])
                    # print(inter)
                    if len(inter) <= 1:
                        continue
                    for x2 in inter:
                        if x2 == x:
                            continue
                        res = min(res, abs(y1 - y2) * abs(x - x2))
        return res if res != float('inf') else 0
