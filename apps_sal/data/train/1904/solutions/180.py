class Solution(object):

    def kClosest(self, points, K):

        def distance(p):
            return (p[0] ** 2 + p[1] ** 2) ** 0.5

        def partition(l, r):
            pivot = points[r]
            mover = l
            for i in range(l, r):
                if distance(points[i]) <= distance(pivot):
                    (points[mover], points[i]) = (points[i], points[mover])
                    mover += 1
            (points[mover], points[r]) = (points[r], points[mover])
            return mover

        def sort(l, r):
            if l < r:
                p = partition(l, r)
                if p == K:
                    return
                elif p < K:
                    sort(p + 1, r)
                else:
                    sort(l, p - 1)
        sort(0, len(points) - 1)
        return points[:K]
