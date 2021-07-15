class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(point):
            return sum([e**2 for e in point])
        
        def partition(nums, left, right):
            x = dist(nums[right])
            i = left - 1
            for j in range(left, right):
                if dist(nums[j]) < x:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[right], nums[i] = nums[i], nums[right]
            return i
        
        p = -1
        left = 0
        right = len(points) - 1
        
        
        while p != K:
            
            p = partition(points, left, right)
            
            if p + 1 < K:
                left = p + 1
            elif p + 1 > K:
                right = p - 1
            else:
                return points[:K]
            
        return points[:K]

# def distSqr(point: List[int]) -> int:
#     d = 0
#     for p in point:
#         d += p ** 2
#     return d

# def partition(points: List[List[int]], left: int, right: int) -> int:
#     if left > right:
#         return -1
#     pivot = left
#     left = left + 1
#     pivotDistSqr = distSqr(points[pivot])
#     while left <= right:
#         if distSqr(points[left]) > pivotDistSqr and distSqr(points[right]) < pivotDistSqr:
#             points[left], points[right] = points[right], points[left]
#             left += 1
#             right -= 1
#         if distSqr(points[left]) <= pivotDistSqr:
#             left += 1
#         if distSqr(points[right]) >= pivotDistSqr:
#             right -= 1
#     points[pivot], points[right] = points[right], points[pivot]
#     pivot = right
#     return pivot

# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         pivot = -1 
#         n = len(points)
#         left, right = 0, n - 1
        
#         while pivot != K - 1:
            
#             pivot = partition(points, left, right)
#             if pivot < K - 1:
#                 left = pivot + 1
#             elif pivot == K - 1:
#                 return points[0:K]
#             elif pivot > K - 1:
#                 right = pivot - 1
#         return points[0:K]


# import heapq
# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         idx = defaultdict(list)
#         heap = []
        
#         for i, p in enumerate(points):
#             d = (p[0] ** 2 + p[1] ** 2)
#             if heap and len(heap) >= K:
#                 if - heap[0] > d:
#                     larger_dist = - heap[0]
#                     idx[larger_dist].pop()
#                     heapq.heappushpop(heap, - d)
#                     idx[d].append(i)
#             else:
#                 heapq.heappush(heap, -d)
#                 idx[d].append(i)
        
#         res = []
#         for indicies in idx.values():
#             for i in indicies:
#                 res.append(points[i])
#         return res

