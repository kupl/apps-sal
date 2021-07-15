class Solution:
    def minCostConnectPoints(self, points:List[List[int]]) -> int:
        \"\"\"
            @params:
                points: List of list of coordinates (in cartesian coordinates)
                where points[i] = [x_i, y_i]
                Are points sorted? Not necessary 
                Can there be negative integers? Yes 
                Can there be duplicate points? No 
                Points length: 1 <= len(points) <= 1000
        
                Test case 1: [[0,0], [1,2], [3,0]]
                expected_output = min((3+3), (3+4)) = 6
                y
                |     
                |
                |  1,2
                |_  _  _ _ _ x 
                0,0    3,0
                 
                Test case 2: [[0,0], [1,1], [2,2]]
                expected_output = min(4, 5) = 4 
                  y
                |     
                |      2,2
                |  1,1
                |   _    _    _ _ _ x 
                0,0           
        \"\"\"
        def manhattan(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        ans, n = 0, len(points)
        seen = set()
        import queue
        q = queue.PriorityQueue()
        q.put((0, (0, 0)))
        
        while len(seen) < n:
            # print(vertices, seen)
            w, (u, v) = q.get()
            if u in seen and v in seen: continue
            ans += w
            seen.add(v)
            for j in range(n):
                if j not in seen and j!=v:
                    q.put((manhattan(points[j], points[v]), (v, j)))
        return ans

        
