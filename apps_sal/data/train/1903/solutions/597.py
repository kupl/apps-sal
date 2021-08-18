class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from queue import PriorityQueue
        q = PriorityQueue()

        l = len(points)
        visited = set()

        for j in range(1, l):
            q.put((abs(points[0][0] - points[j][0]) + abs(points[0][1] - points[j][1]), j))

        visited.add(0)
        count = 1
        ans = 0
        while count < l:
            dis, point = q.get()
            if point not in visited:
                visited.add(point)
                for j in range(l):
                    if j not in visited:
                        q.put((abs(points[point][0] - points[j][0]) + abs(points[point][1] - points[j][1]), j))
                ans += dis
                count += 1
        return ans
