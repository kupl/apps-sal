from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key, value, timestamp):
        self.d[key].append([timestamp, value])

    def get(self, key, timestamp):
        start, end = 0, len(self.d[key]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.d[key][mid][0] == timestamp:
                return self.d[key][mid][1]
            elif self.d[key][mid][0] < timestamp:
                start = mid
            else:
                end = mid
        if self.d[key][end][0] <= timestamp:
            return self.d[key][end][1]
        if self.d[key][start][0] <= timestamp:
            return self.d[key][start][1]
        return ''
