class myObj:
    def __init__(self, val, p):
        self.val = val
        self.p = p

    def __lt__(self, other):
        return self.val > other.val


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        for p in points:
            dis = p[0] * p[0] + p[1] * p[1]
            heapq.heappush(h, myObj(dis, p))
            if len(h) > K:
                heapq.heappop(h)

        ans = []
        while h:
            obj = heapq.heappop(h)
            ans.append(obj.p)
        return ans
