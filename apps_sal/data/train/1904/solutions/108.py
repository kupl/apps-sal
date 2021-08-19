import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-dist, point))
            if len(heap) > K:
                heapq.heappop(heap)

        return [tuple[1] for tuple in heap]

#         left = 0
#         right = len(points) - 1
#         while left <= right:
#             mid = self.helperPivot(left, right, points)
#             if mid == K:
#                 break
#             if mid < K:
#                 left = mid+1
#             else:
#                 right = mid - 1
#         return points[:K]


#     def helperPivot(self,start, end, points):
#         def dist(point):
#             return point[0]**2 + point[1]**2
#         pivot = start
#         left = start + 1
#         right = end
#         while left <= right:
#             if dist(points[left]) > dist(points[pivot]) and dist(points[right]) < dist(points[pivot]):
#                 #swap
#                 points[left], points[right] = points[right], points[left]
#             if dist(points[left]) <= dist(points[pivot]):
#                 left += 1
#             if dist(points[right]) >= dist(points[pivot]):
#                 right -=1
#         #right is the correct position of pivot
#         points[pivot], points[right] = points[right], points[pivot]
#         return right
