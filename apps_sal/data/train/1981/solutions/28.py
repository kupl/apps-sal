class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        heap = []
        dict = defaultdict(int)
        requests.sort()
        count = 0
        start = 0
        for i in requests:
            while heap and heap[0] < i[0]:
                heap_pop = heapq.heappop(heap)
                dict[count] += heap_pop + 1 - start
                start = heap_pop + 1
                count -= 1
            heapq.heappush(heap, i[1])
            dict[count] += i[0] - start
            start = i[0]
            count += 1
        while heap:
            heap_pop = heapq.heappop(heap)
            dict[count] += heap_pop + 1 - start
            start = heap_pop + 1
            count -= 1
        nums.sort(reverse=True)
        index = 0
        res = 0
        sort_key = sorted(list(dict.keys()), reverse=True)
        for key in sort_key:
            res += key * sum(nums[index:index + dict[key]])
            res %= 10 ** 9 + 7
            index += dict[key]
        return res
