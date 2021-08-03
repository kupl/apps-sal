class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        '''
        columns = defaultdict(list)

        for x, y in points:
            columns[x].append(y)

        result = float('inf')
        lastx = {}

        for x in sorted(columns):
            column_list = columns[x]
            column_list.sort()

            for j, y2 in enumerate(column_list):
                for i in range(j):
                    y1 = column_list[i]

                    if (y1, y2) in lastx:
                        result = min(result, (x-lastx[y1,y2]) * (y2-y1))
                    lastx[y1,y2] = x

        return result if result < float('inf') else 0
        '''

        seen = set()
        ans = sys.maxsize

        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    ans = min(ans, area)

            seen.add((x1, y1))

        return ans if ans < sys.maxsize else 0
