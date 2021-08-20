class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def dist(x):
            return x[0] ** 2 + x[1] ** 2

        def partition(start, end):
            ran = random.randint(start, end)
            pivot = end
            (points[pivot], points[ran]) = (points[ran], points[pivot])
            border = start
            for cur in range(start, end):
                if dist(points[cur]) >= dist(points[pivot]):
                    (points[cur], points[border]) = (points[border], points[cur])
                    border += 1
            (points[border], points[pivot]) = (points[pivot], points[border])
            return border

        def quick_sort(left, right, k):
            if left >= right:
                return
            p = partition(left, right)
            if p == k - 1:
                return
            if p < k - 1:
                quick_sort(p + 1, right, k)
            else:
                quick_sort(left, p - 1, k)
        quick_sort(0, len(points) - 1, len(points) - K + 1)
        return points[len(points) - K:]
