class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = sys.maxsize
        diag = collections.defaultdict(set)
        for i, j in points:
            diag[i].add(j)
        
        for i in range(len(points)):
            a1, a2 = points[i]
            for j in range(len(points)):
                b1, b2 = points[j]
                if not (b1 > a1 and b2 > a2):
                    continue
                if b2 in diag[a1] and a2 in diag[b1]:
                    # print(\"?\")
                    res = min(res, abs(a1 - b1) * abs(a2 - b2))
        
        
        return res if res != sys.maxsize else 0
