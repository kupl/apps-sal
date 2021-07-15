class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distant = [[point,point[0]**2+point[1]**2] for point in points]
        distant.sort(key = itemgetter(1))
        res = [distant[i][0] for i in range(K)]
        return res

