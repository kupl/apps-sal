from collections import Counter


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        stCount = Counter([request[0] for request in requests])
        endCount = Counter([request[1] for request in requests])
        tmp = []
        for st, times in stCount.items():
            tmp.append([st, 's', times])
        for end, times in endCount.items():
            tmp.append([end, 'z', times])
        nums.sort(reverse=True)
        tmp.sort()

        segments = []

        times = 0
        prev = 0
        MOD = (10 ** 9) + 7
        for point in tmp:
            if point[1] == 's':
                segments.append([point[0] - prev, times])
                times += point[2]
                prev = point[0]
            if point[1] == 'z':
                segments.append([point[0] - prev + 1, times])
                times -= point[2]
                prev = point[0] + 1

        segments.sort(key=lambda element: element[1], reverse=True)
        st = 0
        ans = 0

        for segment, times in segments:
            for i in range(st, st + segment):
                ans += nums[i] * times
            ans %= MOD
            st = st + segment

        return ans
