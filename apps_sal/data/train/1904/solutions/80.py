class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(i): return points[i][0]**2 + points[i][1]**2

        def quicksort(points, K):
            print(points, K)
            if not points:
                return

            pivot = points[-1]
            l, r, m = [], [], []
            for i in points:
                if dist(i) == dist(pivot):
                    m.append(i)
                elif dist(i) < dist(pivot):
                    l.append(i)
                else:
                    r.append(i)
            if len(l) >= K:
                return quicksort(l, K)
            elif len(l) < K <= len(l) + len(m):
                return l + m[:K - len(l)]
            else:
                return l + m + quicksort(r, K - len(l) - len(m))
        return [points[i] for i in quicksort([i for i in range(len(points))], K)]
