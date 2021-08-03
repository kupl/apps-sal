from collections import deque


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq_arr = [0] * n
        requests.sort()
        starts = deque([request[0] for request in requests])
        requests.sort(key=lambda x: x[1])
        ends = deque([request[1] for request in requests])
        active_intervals = 0
        for pos in range(n):
            while(starts and pos == starts[0]):
                starts.popleft()
                active_intervals += 1
            while(ends and pos == ends[0] + 1):
                ends.popleft()
                active_intervals -= 1
            freq_arr[pos] = active_intervals

        nums.sort(reverse=True)
        freq_arr.sort(reverse=True)
        answer = 0
        for n, f in zip(nums, freq_arr):
            answer += n * f
        return answer % ((10**9) + 7)
