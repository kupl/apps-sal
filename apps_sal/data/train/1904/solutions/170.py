class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point):
            return point[0]**2 + point[1]**2

        def find_pivot_index(low, high, p_index):
            ppoint = points[p_index]
            points[p_index], points[high] = points[high], points[p_index]

            i = low
            j = low

            while j < high:
                if distance(points[j]) < distance(points[high]):
                    points[i], points[j] = points[j], points[i]
                    i += 1
                j += 1

            points[i], points[high] = points[high], points[i]
            return i

        def recursion(low, high):
            pivot_index = random.randint(low, high)
            p = find_pivot_index(low, high, pivot_index)

            if p == k - 1:
                return points[:p + 1]
            elif p < k - 1:
                return recursion(p + 1, high)
            else:
                return recursion(low, p - 1)

        return recursion(0, len(points) - 1)
