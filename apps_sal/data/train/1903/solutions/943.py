class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                l = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append((l, tuple(p1), tuple(p2)))
                
                
        trees = []
        for point in points:
            a = set()
            a.add(tuple(point))
            trees.append(a)
        
        t1 = -1
        t2 = -1
        tot = 0
        for e in sorted(edges):
            l, p1, p2 = e
            for i, tree in enumerate(trees):
                if p1 in tree:
                    t1 = i
                    break
            for i, tree in enumerate(trees):
                if p2 in tree:
                    t2 = i
                    break
                    
            if t1 != t2:
                tot += l
                trees[t1].update(trees[t2])
                del trees[t2]
                
            
        return tot
