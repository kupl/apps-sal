class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def get_distance(point):
            return point[0] ** 2 + point[1] ** 2

        def helper(i, j, K):
            if i >= j:
                return
            pivot_index = random.randint(i, j)
            points[j], points[pivot_index] = points[pivot_index], points[j]
            mid = partition(i, j)
            if mid == K - 1:
                return
            elif mid < K - 1:
                helper(mid + 1, j, K)
            else:
                helper(i, mid - 1, K)

        def partition(i, j):
            left, right = i, j
            pivot_distance = get_distance(points[j])
            for k in range(left, right):
                if get_distance(points[k]) < pivot_distance:
                    points[i], points[k] = points[k], points[i]
                    i += 1
            points[i], points[j] = points[j], points[i]
            return i

        helper(0, len(points) - 1, K)
        return points[:K]


#         def get_distance(point):
#             return point[0] ** 2 + point[1] ** 2

#         def helper(i, j, K):
#             if i >= j:
#                 return
#             pivot_index = random.randint(i, j)
#             points[j], points[pivot_index] = points[pivot_index], points[j]
#             mid = partition(i, j)
#             if mid - i + 1 == K:
#                 return
#             elif mid - i + 1 < K:
#                 helper(mid + 1, j, K - (mid - i + 1))
#             else:
#                 helper(i, mid - 1, K)

#         def partition(i, j):
#             left, right = i, j
#             pivot_distance = get_distance(points[j])
#             for k in range(left, right):
#                 if get_distance(points[k]) < pivot_distance:
#                     points[i], points[k] = points[k], points[i]
#                     i += 1
#             points[i], points[j] = points[j], points[i]
#             return i

#         helper(0, len(points) - 1, K)
#         return points[:K]
