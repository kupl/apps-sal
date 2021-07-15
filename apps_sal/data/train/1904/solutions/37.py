class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dic = collections.defaultdict(list)
        for p in points:
            d = p[0]**2 + p[1]**2
            dic[d].append(p)
        dic2 = list(dic.keys())
        print(dic2)
        heapq.heapify(dic2)
        res = []
        count = 0
        while(count<K):
            res.extend(dic[heapq.heappop(dic2)])
            count = len(res)
        return res
