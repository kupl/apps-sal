import heapq
'\n1584. Min Cost to Connect All Points.  Medium\n\nYou are given an array points representing integer coordinates\nof some points on a 2D-plane, where points[i] = [xi, yi].\n\nThe cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance\nbetween them: |xi - xj| + |yi - yj|,\nwhere |val| denotes the absolute value of val.\n\nReturn the minimum cost to make all points connected.\nAll points are connected if there is exactly one simple path\nbetween any two points.\n\nExample 1:\nInput: points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]\nOutput: 20\nExplanation:\n\nWe can connect the points as shown above to get the minimum cost of 20.\nNotice that there is a unique path between every pair of points.\n\nExample 2:\nInput: points = [[3, 12], [-2, 5], [-4, 1]]\nOutput: 18\n\nExample 3:\nInput: points = [[0, 0], [1, 1], [1, 0], [-1, 1]]\nOutput: 4\n\nExample 4:\nInput: points = [[-1000000, -1000000], [1000000, 1000000]]\nOutput: 4000000\n\nExample 5:\nInput: points = [[0, 0]]\nOutput: 0\n\nConstraints:\n1 <= points.length <= 1000\n-106 <= xi, yi <= 106\nAll pairs (xi, yi) are distinct.\n\nAccepted 1,742 / 5,429 submissions.\n'


def man_dist_4(x, y, u, v):
    return abs(x - u) + abs(y - v)


def man_dist_pt(ptA, ptB):
    return abs(ptA[0] - ptB[0]) + abs(ptA[1] - ptB[1])


class Solution:

    def minCostConnectPoints(self, p: List[List[int]]) -> int:

        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        (ans, n) = (0, len(p))
        seen = set()
        vertices = [(0, (0, 0))]
        while len(seen) < n:
            (w, (u, v)) = heapq.heappop(vertices)
            if u in seen and v in seen:
                continue
            ans += w
            seen.add(v)
            for j in range(n):
                if j not in seen and j != v:
                    heapq.heappush(vertices, (manhattan(p[j], p[v]), (v, j)))
        return ans


class SolutionTle:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        points.sort()
        lost = {(x, y) for (x, y) in points}
        found = set()
        (x, y) = lost.pop()
        found.add((x, y))
        minc = float('inf')
        for (u, v) in lost:
            md = man_dist_4(x, y, u, v)
            if minc > md:
                minc = md
                minu = u
                minv = v
        cost = minc
        lost.remove((minu, minv))
        found.add((minu, minv))
        while lost:
            minc = float('inf')
            for (x, y) in found:
                for (u, v) in lost:
                    md = man_dist_4(x, y, u, v)
                    if minc > md:
                        minc = md
                        minu = u
                        minv = v
            cost += minc
            lost.remove((minu, minv))
            found.add((minu, minv))
        return cost
