class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []

        def insert(d, pos):
            l = 0
            r = len(res)
            while l < r:
                mid = (l + r) // 2
                if res[mid][0] > d:
                    r = mid
                else:
                    l = mid + 1
            res.insert(l, [d, pos])
            Max = res[-1][0]
        Max = float('inf')

        for i in range(len(points)):
            dis = (points[i][0])**2 + (points[i][1])**2
            print(len(res))
            if i > K:
                res.pop()
            insert(dis, points[i])
        ans = []
        for i in range(K):
            ans.append(res[i][1])
        return ans
