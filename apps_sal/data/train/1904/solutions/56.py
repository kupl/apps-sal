from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def dst(point):
            return (point[0] ** 2 + point[1] ** 2) ** (1 / 2)

        n = 0
        q = PriorityQueue()
        for point in points:
            point = [-dst(point)] + point[:]
            if n < K:
                q.put(point)

            else:
                least = q.get()

                if -point[0] < -least[0]:
                    q.put(point)
                else:
                    q.put(least)
            n += 1

        closest = []
        while not q.empty():
            closest.append(q.get()[1:])

        return closest
