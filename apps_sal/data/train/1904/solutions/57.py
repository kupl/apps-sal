class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        li = []

        class Point:

            def __init__(self, x, y):
                self.x = x
                self.y = y

            def distance_square(self):
                return self.x * self.x + self.y * self.y

            def __lt__(self, other):
                return self.distance_square() < other.distance_square()
        for p in points:
            x = p[0]
            y = p[1]
            pt = Point(x, y)
            heapq.heappush(li, pt)
        result_p = [heapq.heappop(li) for i in range(K)]
        result = [[p.x, p.y] for p in result_p]
        return result
