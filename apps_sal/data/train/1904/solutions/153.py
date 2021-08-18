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
