class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def partition(start, end):
            pivot = start
            left = start + 1
            right = end
            while True:
                while left < right and comparer(points[pivot], points[left]):
                    left += 1
                while left <= right and comparer(points[right], points[pivot]):
                    right -= 1
                if left >= right:
                    break
                (points[left], points[right]) = (points[right], points[left])
            (points[pivot], points[right]) = (points[right], points[pivot])
            return right

        def comparer(point1, point2):
            return point1[0] ** 2 + point1[1] ** 2 >= point2[0] ** 2 + point2[1] ** 2
        (left, right, mid) = (0, len(points) - 1, 0)
        while left <= right:
            mid = partition(left, right)
            if mid == K - 1:
                break
            elif mid > K - 1:
                right = mid - 1
            else:
                left = mid + 1
        return points[:K]
