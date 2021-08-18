class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        max_pts = 500
        dis = [[0 for _ in range(max_pts)] for _ in range(max_pts)]

        def getPointsInside(i, r, n):
            angles = []

            for j in range(n):
                if i != j and dis[i][j] <= 2 * r:
                    B = math.acos(dis[i][j] / (2 * r))

                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    A = math.atan2(y1 - y2, x1 - x2)
                    alpha = A - B
                    beta = A + B
                    angles.append((alpha, False))
                    angles.append((beta, True))

            angles.sort()
            cnt, res = 1, 1
            for angle in angles:
                if angle[1] == 0:
                    cnt += 1
                else:
                    cnt -= 1

                res = max(cnt, res)

            return res

        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dis[i][j] = dis[j][i] = sqrt((x1 - x2)**2 + (y1 - y2)**2)

        ans = 0
        for i in range(n):
            ans = max(ans, getPointsInside(i, r, n))

        return ans
