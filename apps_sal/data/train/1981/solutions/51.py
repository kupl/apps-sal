class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        freq = [0] * n
        heap = []
        requests.sort()
        j = 0
        for i in range(n):
            while j < len(requests) and requests[j][0] <= i:
                heapq.heappush(heap, (requests[j][1], requests[j][0]))
                j += 1
            while heap and heap[0][0] < i:
                heapq.heappop(heap)
            freq[i] = len(heap)
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        return sum([freq[i] * nums[i] for i in range(n)]) % mod
