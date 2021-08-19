class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distanceList = []
        for (x, y) in points:
            distanceList.append((x, y, self.distanceFromOrigin(x, y)))
        return [[p[0], p[1]] for p in heapq.nsmallest(K, distanceList, key=lambda x: x[2])]

    def distanceFromOrigin(self, x, y):
        return sqrt(pow(x - 0, 2) + pow(y - 0, 2))
