class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def getpoints(l, i, r, n, dis):
            d = {}
            pi = 3.1415626
            angles = []
            for j in range(n):
                if i != j and dis[i][j] <= 2 * r:
                    # print(dis[i][j]/(2*r))
                    B = math.acos(dis[i][j] / (2 * r))
                    A = math.acos((l[j][0] - l[i][0]) / dis[i][j])
                    if l[j][1] - l[i][1] < 0:
                        A = 2 * pi - A
                    a = A - B
                    b = A + B
                    # print(i,j,(A/3.14)*180,(B*180/3.14))
                    angles.append((a, 0))  # start
                    angles.append((b, 1))  # end

            angles.sort()
            # print(l[i],angles)
            ct = 1
            res = 1
            for a in angles:
                if a[1] == 0:
                    ct += 1
                else:
                    ct -= 1
                res = max(res, ct)
            # print(i,res)
            return res
        n = len(points)
        dis = [[0 for j in range(n)] for i in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                dis[i][j] = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**(0.5)
                dis[j][i] = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**(0.5)
        ans = 0
        # print(dis)
        # print(dis[0][3],dis[3][0])
        for i in range(n):
            ans = max(ans, getpoints(points, i, r, n, dis))
        return ans
