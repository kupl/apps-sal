class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n1 = len(points)
        newList = [0] * n1
        for i in range(n1):
            pointX = points[i][0]
            pointY = points[i][1]
            d2 = pointX * pointX + pointY * pointY
            newList[i] = d2
        newList.sort()
        res = newList[K - 1]
        i = 0
        t = 0
        ans = []
        while i < n1 and t < K:
            if res >= points[i][0] * points[i][0] + points[i][1] * points[i][1]:
                ans = ans + [points[i]]
                t += 1
            i += 1
        return ans
