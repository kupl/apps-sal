\"\"\"
https://www.youtube.com/watch?v=pFgBZFKJ2Co
fast forward to 17minutes

Group the points by x coordinates, so that we have columns of points. Then, for every pair of points in a column (with coordinates (x,y1) and (x,y2)), check for the smallest rectangle with this pair of points as the rightmost edge. We can do this by keeping memory of what pairs of points we've seen before.

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

columns = {
  # x: y1, y1
    1: 1, 3
    3: 1, 3
    4: 1, 3
}

lastx {
    (1,3) : 1 -> 3      # (y1, y2) : x axis
}
            i
            y2
column = [1,3]
            j
            y1 
\"\"\"
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) <= 3: return 0
        columns = collections.defaultdict(list)
        for x,y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')
        
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for i, y2 in enumerate(column):
                for j in range(i):
                    y1 = column[j]
                    if (y1, y2) in lastx:
                        area = (x - lastx[y1, y2]) * (y2 - y1)
                        ans = min(ans, area)
                    lastx[y1, y2] = x
        
        return ans if ans < float('inf') else 0
            
