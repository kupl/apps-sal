from collections import OrderedDict


class Solution:

    def partition(self, nums, l, r):
        piv = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= piv:
                i += 1
                (nums[i], nums[j]) = (nums[j], nums[i])
        (nums[r], nums[i + 1]) = (nums[i + 1], nums[r])
        return i + 1

    def selectSort(self, nums, left, right, k):
        if left < right:
            p = self.partition(nums, left, right)
            if p == k:
                return
            elif k < p:
                self.selectSort(nums, left, p - 1, k)
            else:
                self.selectSort(nums, p + 1, right, k)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dists = [math.sqrt(p[0] ** 2 + p[1] ** 2) for p in points]
        self.selectSort(dists, 0, len(dists) - 1, K)
        print(dists)
        out = []
        if K == len(points):
            return points
        for p in points:
            if math.sqrt(p[0] ** 2 + p[1] ** 2) < dists[K]:
                out.append(p)
        return out
