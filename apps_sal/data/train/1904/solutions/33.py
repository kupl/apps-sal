#     Version I sort:
#       Step1: write a comparator
#       Step2: write a distance calculator
#       Step3: sort
#       T: O(nlgn) S: O(n)
#     Version II: k sort
#       T: O(nlgk) S: O(k)
#     Version III: quick select
#       Step1: start, end
#       Step2: find mid and seperate to left part and right part
#       Step3: check if mid == k: return [:mid] or check mid again in right part or left part again
#       T: O(n) S: O(lgn) the height of stack
class Solution:
    def _getDistance(self, point):
        dis = math.sqrt(point[0]**2 + point[1]**2)
        return dis

    def _partition(self, start, end, points):
        target = points[start]
        while start < end:
            while start < end and self._getDistance(points[end]) >= self._getDistance(target):
                end -= 1
            points[start] = points[end]
            while start < end and self._getDistance(points[start]) <= self._getDistance(target):
                start += 1
            points[end] = points[start]
        points[start] = target
        return start

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        start = 0
        end = len(points) - 1
        while start <= end:
            mid = self._partition(start, end, points)
            if mid == K:
                return points[:K]
            elif mid > K:
                end = mid - 1
            else:
                start = mid + 1
        return points[:K]
