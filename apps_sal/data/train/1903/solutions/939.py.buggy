class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        params = {}
        for x, i in enumerate(points):
            for j in points[x+1:]:
                s = str(i[0]) + \" \" + str(i[1]) + \" \" + str(j[0]) + \" \" + str(j[1])
                params[s] = abs(i[0]-j[0])+abs(i[1]-j[1])
        d = {k: v for k, v in sorted(params.items(), key=lambda item: item[1])}
        ds = []
        vl = {}
        v = 0
        for i in d:
            ln1, rn1, ln2, rn2 = i.split()
            v1 = -1
            v2 = -1
            for y, j in enumerate(ds):
                if ln1+\" \"+rn1 in j:
                    v1 = y
                if ln2+\" \"+rn2 in j:
                    v2 = y
            if v1 < 0 and v2 < 0:
                ds.append({ln1+\" \" +rn1, ln2+\" \" +rn2})
            elif v1 == v2:
                continue
            elif v1 < 0 and v2 >= 0:
                ds[v2] = ds[v2].union({ln1+\" \" +rn1})
                vl[ln1+\" \" +rn1] = True
            elif v1 >= 0 and v2 < 0:
                ds[v1] = ds[v1].union({ln2+\" \" +rn2})
                vl[ln2+\" \" +rn2] = True
            elif v1 != v2:
                n = ds[v1].union(ds[v2])
                if v2 > v1:
                    ds.pop(v2)
                    ds.pop(v1)
                else:
                    ds.pop(v1)
                    ds.pop(v2)
                ds.append(n)
            v += d[i]
            if len(ds) == 1 and len(ds[0]) == len(points):
                return v
        return v
        
                
                
