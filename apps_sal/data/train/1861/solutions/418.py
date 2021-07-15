class Solution(object):
    def minAreaRect(self, points):
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
# class Solution:
#     def minAreaRect(self, points: List[List[int]]) -> int:
#         d_x = collections.defaultdict(set)
#         d_y = collections.defaultdict(set)
#         for x, y in points: 
#             d_x[x].add(y)
#             d_y[y].add(x)
#         area = sys.maxsize            
#         for x, y in points:
#             for yy in d_x[x]: # find same x (point above), larger y
#                 if yy <= y: continue
#                 for xx in d_y[y]: # find same y (point right), larget x
#                     if xx > x and yy in d_x[xx]:
#                         area = min(area, (xx-x)*(yy-y))
#         return area if area != sys.maxsize else 0

