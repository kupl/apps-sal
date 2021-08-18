class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        if not points:
            return []

        def distance(x, y):

            return ((x - 0)**2 + (y - 0)**2)**0.5

        def binsea_insert(dist, point):

            if not nearest:
                nearest.append((dist, point))
                return

            left, right = 0, len(nearest) - 1

            while left <= right:

                d, coor = nearest[right]
                if dist >= d:
                    nearest.insert(right + 1, (dist, point))
                    return

                d, coor = nearest[left]

                if dist <= d:
                    nearest.insert(left, (dist, point))
                    return

                mid = left + (right - left) // 2

                d, coor = nearest[mid]

                if dist < d:
                    right = mid - 1

                else:
                    left = mid + 1

        nearest = []

        for point in points:
            x, y = point
            binsea_insert(distance(x, y), point)

        print(nearest)
        results = []
        for k in range(K):
            if k < len(nearest):
                d, point = nearest[k]
                results.append(point)

        return results
