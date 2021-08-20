class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        nums = []
        heapq.heapify(nums)

        def dist(x, y):
            return (x ** 2 + y ** 2) ** 0.5
        for (x, y) in points:
            heapq.heappush(nums, (-dist(x, y), [x, y]))
            if len(nums) > K:
                heapq.heappop(nums)
        return [k[1] for k in nums]
