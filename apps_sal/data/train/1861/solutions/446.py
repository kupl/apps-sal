class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = collections.defaultdict(list)
        res = float('inf')

        for x, y in points:
            columns[x].append(y)
        y_pairs = dict()
        for x in sorted(columns):
            ys = sorted(columns[x])
            for i in range(len(ys) - 1):
                for j in range(i + 1, len(ys)):
                    if (ys[i], ys[j]) in y_pairs:
                        res = min(res, (x - y_pairs[(ys[i], ys[j])]) * (ys[j] - ys[i]))
                    y_pairs[(ys[i], ys[j])] = x
        return res if res != float('inf') else 0
