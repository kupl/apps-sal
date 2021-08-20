class Solution:

    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                (nums[i], nums[j]) = (nums[j], nums[i])
        (nums[i + 1], nums[r]) = (nums[r], nums[i + 1])
        return i + 1

    def selectSort(self, nums, l, r, k):
        if l < r:
            p = self.partition(nums, l, r)
            if p == k:
                return
            elif k < p:
                self.selectSort(nums, l, p - 1, k)
            else:
                self.selectSort(nums, p + 1, r, k)

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
