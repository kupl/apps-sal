class Solution:
    import heapq

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        res = [[] for i in range(len(nums))]
        heap = []
        for request in requests:
            res[request[0]].append(request[1])
        countNum = [0] * len(nums)
        for i in range(len(res)):
            if res[i]:
                for element in res[i]:
                    heapq.heappush(heap, element)
            countNum[i] += len(heap)
            while heap and heap[0] == i:
                heapq.heappop(heap)
        countNum.sort(reverse=True)
        count = 0
        for i in range(len(nums)):
            count += nums[i] * countNum[i] % (10 ** 9 + 7)
        return count % (10 ** 9 + 7)
