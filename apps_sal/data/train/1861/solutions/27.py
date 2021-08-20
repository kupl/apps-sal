class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        record = {}
        points.sort(key=lambda x: [x[0], x[1]])
        res = float('inf')
        temp = [points[0][1]]
        for i in range(1, len(points)):
            if points[i][0] == points[i - 1][0]:
                temp.append(points[i][1])
            else:
                if len(temp) >= 2:
                    for j in range(len(temp) - 1):
                        for k in range(j + 1, len(temp)):
                            if (temp[j], temp[k]) in record:
                                res = min(res, (points[i - 1][0] - record[temp[j], temp[k]]) * (temp[k] - temp[j]))
                            record[temp[j], temp[k]] = points[i - 1][0]
                temp = [points[i][1]]
        if len(temp) >= 2:
            for j in range(len(temp) - 1):
                for k in range(j + 1, len(temp)):
                    if (temp[j], temp[k]) in record:
                        res = min(res, (points[-1][0] - record[temp[j], temp[k]]) * (temp[k] - temp[j]))
        if res == float('inf'):
            return 0
        return res
