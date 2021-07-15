\"\"\"
https://www.youtube.com/watch?v=pFgBZFKJ2Co
fast forward to 17minutes

Group the points by x coordinates, so that we have columns of points. Then, for every pair of points in a column (with coordinates (x,y1) and (x,y2)), check for the smallest rectangle with this pair of points as the rightmost edge. We can do this by keeping memory of what pairs of points we've seen before.

columns = {
    1: 1, 3
    3: 1, 3
    4: 1, 4
    
}

column = [1,3]
\"\"\"
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # dictionary that stores a list of x coordinates for each vertical edge (y1, y2) where y1 < y2
        x_coord = collections.defaultdict(list) 
        points.sort(key = lambda x: (x[0], x[1])) # For making traversal more convenient
        min_area = float('inf')
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2: # This is a vertical edge.
                    if (y1, y2) in x_coord: # We have seen this vertical edge in the past.
                        x_other = x_coord[(y1, y2)][-1] # Recall: we traverse points in the order of inceasing x
                        min_area = min(min_area, (y2-y1) * (x1 - x_other)) # Update min area
                    x_coord[(y1, y2)].append(x1)
        return min_area if min_area!=float('inf') else 0
