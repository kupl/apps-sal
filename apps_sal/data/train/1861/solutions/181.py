class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        p = collections.defaultdict(set)
        for x, y in points:
            p[x].add(y)
        xs = sorted(p.keys())
        minv = float('inf')
        for i in range(len(xs) - 1):
            for j in range(i + 1, len(xs)):
                le = xs[j] - xs[i]
                if le > minv:
                    break
                potential = sorted(p[xs[i]].intersection(p[xs[j]]))
                #print(le, potential)
                v = float('inf')
                for j in range(len(potential) - 1):
                    v = min(v, potential[j + 1] - potential[j])
                minv = min(minv, v * le)
        return minv if minv < float('inf') else 0
