class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set()
        x_map, y_map = defaultdict(set), defaultdict(set)
        for x, y in points:
            point_set.add((x, y))
            x_map[x].add((x, y))
            y_map[y].add((x, y))
        
        min_rec = math.inf
        def dfs(points:list):
            nonlocal x_map, y_map, point_set, min_rec
            if len(points) not in (1, 2, 3):
                return 
            if len(points) == 1:
                x, y = points[0]
                for point in x_map[x]:
                    if point[1] < y:
                        points.append(point)
                        dfs(points)
                        points.pop()
            elif len(points) == 2:
                x, y = points[0]
                for point in y_map[y]:
                    if point[0] > x:
                        points.append(point)
                        dfs(points)
                        points.pop()
            else:
                x2, y1 = points[2][0], points[1][1]
                if (x2, y1) in point_set:
                    x1, y2 = points[1][0], points[2][1]
                    min_rec = min(min_rec, (x2 - x1) * (y2 - y1))
        for point in point_set:
            dfs([point])
        if min_rec != math.inf:
            return min_rec
        else:
            return 0

