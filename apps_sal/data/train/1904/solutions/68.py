class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from queue import PriorityQueue as pq
        distance_points = [(-1 * (x ** 2 + y ** 2) ** 0.5, [x, y]) for (x, y) in points]
        q = pq()
        for item in distance_points:
            if q.qsize() < k:
                q.put(item)
            else:
                (distance, _) = item
                popped = q.get()
                (popped_distance, _) = popped
                if distance > popped_distance:
                    q.put(item)
                else:
                    q.put(popped)
        return [q.get()[1] for _ in range(k)]
