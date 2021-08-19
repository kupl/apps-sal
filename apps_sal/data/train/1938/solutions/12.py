MOD = 10 ** 9 + 7


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:

        allY = []
        for x1, y1, x2, y2 in rectangles:
            allY.append((y1, 0, x1, x2))
            allY.append((y2, 1, x1, x2))
        allY.sort()

        allX, ans = [], 0
        curHeight = allY[0][0]

        for y, t, x1, x2 in allY:
            ans += self.getX(allX) * (y - curHeight)
            ans %= MOD
            if t == 0:
                bisect.insort(allX, (x1, x2))
            else:
                idx = bisect.bisect_left(allX, (x1, x2))
                #print(idx, x1, x2, allX)
                allX.pop(idx)
                #allX.remove((x1, x2))

            curHeight = y

        return ans

    def getX(self, allX):
        ans = 0
        cur = -1
        for x1, x2 in allX:
            cur = max(cur, x1)
            ans += max(0, x2 - cur)
            cur = max(cur, x2)
        return ans
