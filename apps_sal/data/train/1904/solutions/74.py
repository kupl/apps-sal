from queue import PriorityQueue
import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        queue = PriorityQueue()

        for point in points:
            queue.put((math.sqrt((point[0])**2 + (point[1])**2), point))

        ans = []

        for i in range(K):
            ans.append(queue.get()[1])
        return ans
