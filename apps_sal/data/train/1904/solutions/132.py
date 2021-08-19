class myObj:

    def __init__(self, val, p):
        self.val = val
        self.p = p

    def __lt__(self, other):
        return self.val < other.val


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def partition(arr, left, right):
            i = left
            for j in range(left, right):
                if arr[j] < arr[right]:
                    (arr[i], arr[j]) = (arr[j], arr[i])
                    i += 1
            (arr[i], arr[right]) = (arr[right], arr[i])
            return i

        def sort(arr, left, right, K):
            if left < right:
                p = partition(arr, left, right)
                if p == K:
                    return
                elif p < K:
                    sort(arr, p + 1, right, K)
                else:
                    sort(arr, left, p - 1, K)
        dis = [0] * len(points)
        for i in range(len(points)):
            dis[i] = myObj(points[i][0] * points[i][0] + points[i][1] * points[i][1], points[i])
        sort(dis, 0, len(points) - 1, K)
        ans = []
        for i in range(K):
            ans.append(dis[i].p)
        return ans
