class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        # points = sorted(points, key = lambda x: x[0]**2 + x[1]**2)
        # return points [:K]

        distance_dict = dict()

        def distance(xy):
            xy = tuple(xy)
            if xy in distance_dict:
                return distance_dict[xy]
            ans = xy[0]**2 + xy[1]**2
            distance_dict[xy] = ans
            return ans

        def _quicksort(points, left, right):

            if left > right:
                return

            pivot = right
            lower = left
            for i in range(left, right):
                if distance(points[i]) <= distance(points[pivot]):
                    points[lower], points[i] = points[i], points[lower]
                    lower = lower + 1

            pivot = lower
            points[pivot], points[right] = points[right], points[pivot]

            if (K - 1) <= pivot:
                _quicksort(points, left, pivot - 1)
            else:
                _quicksort(points, left, pivot - 1)
                _quicksort(points, pivot + 1, right)

            return

        _quicksort(points, 0, len(points) - 1)

        return points[:K]
