import collections
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s= set(map(tuple,points))
        dx = collections.defaultdict(list)
        dy = collections.defaultdict(list)
        for item in points:
            dx[item[0]].append(item[1])
            dy[item[1]].append(item[0])
        
        res = float(\"inf\")
        for x in sorted(dx.keys()):
            for i in range(len(dx[x])):
                y1 = dx[x][i]
                for j in range(i+1,len(dx[x])):
                    y2 = dx[x][j]
                    for x1 in dy[y2]:
                        if x1<=x:
                            continue
                        if (x1,y1) in s:
                            res = min(res,abs(x1-x)*abs(y1-y2))
        if res ==float(\"inf\"):
            return 0
        return res 
