from collections import defaultdict


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count_map = defaultdict(lambda: 0)

        sorted_requests_start = sorted(requests, key=lambda x: x[0])
        sorted_requests_end = sorted(requests, key=lambda x: x[1])
        max_i = len(nums)
        start_ptr = 0
        ended_ptr = 0

        ongoing_request_list = []
        curr_request_count = 0
        for i in range(max_i):
            while start_ptr < len(requests) and sorted_requests_start[start_ptr][0] == i:
                curr_request_count += 1
                start_ptr += 1
            while ended_ptr < len(requests) and sorted_requests_end[ended_ptr][1] < i:
                curr_request_count -= 1
                ended_ptr += 1
            ongoing_request_list.append(curr_request_count)

        sorted_pairs = sorted(ongoing_request_list, key=lambda x: -x)
        sorted_nums = sorted(nums, key=lambda x: -x)

        return int(sum(map(lambda x, y: x * y, sorted_pairs, sorted_nums)) % (1e9 + 7))
