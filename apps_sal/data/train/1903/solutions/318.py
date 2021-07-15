import heapq
'''
1584. Min Cost to Connect All Points.  Medium

You are given an array points representing integer coordinates
of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
between them: |xi - xj| + |yi - yj|,
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected.
All points are connected if there is exactly one simple path
between any two points.

Example 1:
Input: points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3, 12], [-2, 5], [-4, 1]]
Output: 18

Example 3:
Input: points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
Output: 4

Example 4:
Input: points = [[-1000000, -1000000], [1000000, 1000000]]
Output: 4000000

Example 5:
Input: points = [[0, 0]]
Output: 0

Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.

Accepted 1,742 / 5,429 submissions.
'''
def man_dist_4(x,y,u,v):
    return abs(x - u) + abs(y - v)

def man_dist_pt(ptA, ptB):
    return abs(ptA[0] - ptB[0]) + abs(ptA[1] - ptB[1])


class Solution:

    def minCostConnectPoints(self, p: List[List[int]]) -> int:

        def manhattan(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        ans, n = 0, len(p)
        seen = set()
        vertices = [(0, (0, 0))]

        while len(seen) < n:
            # print(vertices, seen)
            w, (u, v) = heapq.heappop(vertices)
            if u in seen and v in seen: continue
            ans += w
            seen.add(v)
            for j in range(n):
                if j not in seen and j!=v:
                    heapq.heappush(vertices, (manhattan(p[j], p[v]), (v, j)))
        return ans

###############################################################################

class SolutionTle:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        points.sort()
        lost = {(x, y) for x, y in points}
        found = set()

        x, y = lost.pop()
        found.add((x, y))
        minc = float('inf')
        for u, v in lost:
            md = man_dist_4(x,y,u,v)
            if minc > md:
                minc = md
                minu = u
                minv = v
        cost = minc
        lost.remove((minu, minv))
        found.add((minu, minv))

        while lost:
            minc = float('inf')
            for x, y in found:
                for u, v in lost:
                    md = man_dist_4(x,y,u,v)
                    if (minc > md):
                        minc = md
                        minu = u
                        minv = v
            cost += minc
            lost.remove((minu, minv))
            found.add((minu, minv))

        return cost


