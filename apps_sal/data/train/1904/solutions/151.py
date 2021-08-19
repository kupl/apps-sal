class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def getDistance(p: List[int]):
            return p[0] ** 2 + p[1] ** 2

        def helper(points: List[List[int]], K: int):
            if len(points) == K:
                return points
            (left, right) = ([], [])
            import random
            random.shuffle(points)
            pivot = points[0][0]
            for point in points:
                curr_distance = point[0]
                if curr_distance > pivot:
                    right.append(point)
                else:
                    left.append(point)
            if len(left) >= K:
                return helper(left, K)
            else:
                return left + helper(right, K - len(left))
        distances = []
        for point in points:
            distances.append([getDistance(point), point])
        top_results = helper(distances, K)
        for (i, result) in enumerate(top_results):
            top_results[i] = result[1]
        return top_results
