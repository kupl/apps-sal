class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        result = float('inf')
        columns = collections.defaultdict(lambda: [])
        for x, y in points:
            columns[x].append(y)

        print('columns is: ' + str(columns))

        # Map from (y1, y2) pair to x
        lastSeen = {}
        for x in sorted(columns.keys()):
            column = sorted(columns[x])
            for i in range(len(column)):
                y1 = column[i]
                for j in range(i + 1, len(column)):
                    if y1 != column[j]:
                        y2 = column[j]
                        if (y1, y2) in lastSeen:
                            prev_x = lastSeen[(y1, y2)]
                            result = min(result, (y2 - y1) * (x - prev_x))
                        lastSeen[(y1, y2)] = x
        return 0 if result == float('inf') else result
