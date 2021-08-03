class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(list)
        lastx = {}
        ans = sys.maxsize

        for x, y in points:
            columns[x].append(y)

        for x in sorted(columns):
            y_list = columns[x]
            y_list.sort()
            for i, y1 in enumerate(y_list):
                for j in range(i):
                    y2 = y_list[j]

                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[(y1, y2)]) * (y1 - y2))

                    lastx[(y1, y2)] = x

        return ans if ans < sys.maxsize else 0

        '''
        seen = set()
        ans = sys.maxsize
        
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1-x2) * abs(y1-y2)
                    ans = min(ans, area)
            
            seen.add((x1,y1))
        
        return ans if ans < sys.maxsize else 0
        '''
