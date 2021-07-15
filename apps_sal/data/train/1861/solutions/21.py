class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], x[1]))
        # print(points)
        mx_y = defaultdict(list)
        for x, y in points:
            mx_y[x].append(y)
        
        # print(mx_y)
        res = float('inf')
        seenY_pairs = {}
        
        for x in mx_y:
            if len(mx_y[x])<2: continue
            for i in range(len(mx_y[x])-1):
                y1 = mx_y[x][i]
                for j in range(i+1, len(mx_y[x])):
                    y2 = mx_y[x][j]
                    
                    if (y1, y2) in seenY_pairs:
                        width = x - seenY_pairs[(y1, y2)]
                        height = y2 - y1
                        res = min(res, width*height)
                    seenY_pairs[(y1, y2)] = x
        
        if res == float('inf'):
            return 0
        else:
            return res
        
# [[1,1],[1,3],[3,1],[3,3],[2,2]]
# [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]

