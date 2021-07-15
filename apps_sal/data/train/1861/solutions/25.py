class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:


        s = set(map(tuple, points))
        dx = collections.defaultdict(list)
        dy = collections.defaultdict(list)
        for x,y in points:
            dx[x].append(y)
            dy[y].append(x)

        res = float('inf')
        for x in sorted(dx.keys()): # 1. find x in dx
            for i in range(len(dx[x])): # 2. find y1, y2 in dx[x]
                y1 = dx[x][i]
                for j in range(i+1, len(dx[x])):
                    y2 = dx[x][j]
                    for x1 in dy[y2]: # 3. find x1 in dy[y2]
                        # always make x in the left side
                        if x1 <= x: continue
                        if (x1, y1) in s: # 4. judeg (x1,y1) in points
                            res = min(res, abs(x-x1) * abs(y1-y2))

        return res if res != float('inf') else 0
