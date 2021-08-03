class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance(point):
            return (point[0]**2 + point[1]**2)**(0.5)

        def partition(left, right, pivot_index):
            pivot = points[pivot_index]
            # move the pivot to the position of right first
            points[pivot_index], points[right] = points[right], points[pivot_index]

            store_index = left
            for i in range(left, right):
                if distance(points[i]) < distance(pivot):
                    points[store_index], points[i] = points[i], points[store_index]
                    store_index += 1

            # move the pivot back to its correct position:
            # such that all elements on the left are smaller, and elements on the right have larger distance to origin.
            points[store_index], points[right] = points[right], points[store_index]

            return store_index

        left, right = 0, len(points) - 1
        while True:
            pivot_index = random.randint(left, right)
            M = partition(left, right, pivot_index)
            if M == K - 1:
                break
            elif M < K - 1:
                left = M + 1
            else:
                right = M - 1

        return points[:K]
