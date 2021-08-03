class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points or not K:
            return []

        distances = []
        disMap = defaultdict(list)
        maxKDis = float('-inf')
        for point in points:
            dis = (point[0] ** 2 + point[1] ** 2) ** 0.5
            disMap[dis].append(point)
            if len(distances) < K:
                distances.append(dis)
                maxKDis = max(maxKDis, dis)
            elif len(distances) >= K and dis < maxKDis:
                distances.sort()
                distances.pop()
                distances.append(dis)
                maxKDis = max(distances[-2:])

        res = []
        for dis in distances:
            res.extend(disMap[dis])

        return res[:K]
