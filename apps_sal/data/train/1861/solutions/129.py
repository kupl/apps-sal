\"\"\"
Inputs
    points (List[List[int]]): x y locations of points
Outputs
    int: minimum area of a rectangle
Notes
    - if no rectangle possible, output 0

Examples
    
    Example 1
        
        Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
        Output: 4
    
    Example 2

        Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
        Output: 2

Ideas
    - distance doesn't tell us if points are parallel or not
    
    - keep track of points at common x and y locations
        const_x: {1: index 0, index 1}
        const_y: {1: index 0, index 2}
        
    - sorting points may help us
    
    - area calc
        + dx * dy
    
    - find two points at same x, and different y
        + then find another two points at different x and same y
            x1, y1
            x2, y2
            x1 = x2
        + then find one point at same y1, different x
            x3, y3
            
            y1 = y3
            
        + then find one point at same y2, different x
            
            x4, y4
            
            x3 = x4
            y2 = y4
    
    - checking for points will be easier with set or hash
        O(1) checks.
        + we need the (x,y) values to verify this

\"\"\"

from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        \"\"\"
        
        - aggreate points by common x or y coordinate
        - 
        
        \"\"\"
        
        ans = float('inf')
        
        ''' Aggregate points by common location '''
        const_x = defaultdict(list)
        
        for point in points:
            x, y = point
            const_x[x].append(y)
        
        ''' Iterate over constant x pairs'''
        
        prev_x = {}  # store x location for pairs of points
        
        for x in sorted(const_x):
            n: int = len(const_x[x])
                
            # Sort by y value
            const_x[x].sort()
            
            for ix in range(n):
                for jx in range(ix + 1, n):
                
                    y1 = const_x[x][ix]  # (x1, y1) smaller y
                    y2 = const_x[x][jx]  # (x1, y2) larger y
                    
                    dy = y2 - y1
                    
                    # Find points at the same y and different x from current
                    # but same x as each other
                    if (y1, y2) in prev_x:
                        dx = x - prev_x[(y1, y2)]
                        ans = min(ans, dx * dy)
                    
                    # Save the x location for every pair of y points
                    prev_x[(y1, y2)] = x
                     
        
        if ans != float('inf'):
            return ans
        else:
            return 0
        
