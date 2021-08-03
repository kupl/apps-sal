from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = PriorityQueue()
        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            if i < K:
                pq.put((-distance, points[i]))
            else:
                pq.put((-distance, points[i]))
                pq.get()
        ans = []
        while pq.qsize() > 0:
            ans.append(pq.get()[1])
        return ans
