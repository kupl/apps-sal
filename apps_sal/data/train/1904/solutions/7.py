from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = PriorityQueue()

        for i, point in enumerate(points):
            point_distance = point[0]**2 + point[1]**2
            if i < K:
                pq.put((-point_distance, point))

            if i >= K:
                min_point_distance, min_point = pq.queue[0]

                if point_distance < -min_point_distance:
                    pq.get()
                    pq.put((-point_distance, point))

        results = []
        while not pq.empty():
            _, point = pq.get()
            results.append(point)
        return results
