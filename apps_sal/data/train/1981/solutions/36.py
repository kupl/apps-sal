class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        start = collections.defaultdict(int)
        end = collections.defaultdict(int)
        min_start = 10000
        max_end = 0
        for request in requests:
            start[request[0]] += 1
            end[request[1]] += 1
            min_start = min(min_start, request[0])
            max_end = max(max_end, request[1])

        cnt = 0
        cnt_dic = {}
        for num in range(min_start, max_end + 1):
            if num in start:
                cnt += start[num]
            if cnt > 0:
                cnt_dic[num] = cnt
            if num in end:
                cnt -= end[num]

        cnt_sorted = sorted(cnt_dic.values(), key=lambda x: -x)
        num_sorted = sorted(nums, key=lambda x: -x)
        result = 0
        for i, cnt in enumerate(cnt_sorted):
            result += num_sorted[i] * cnt
        return result % 1000000007
