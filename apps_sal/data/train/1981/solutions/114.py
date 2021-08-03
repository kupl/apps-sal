class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        tmp = sorted([k for i, j in requests for k in [(i, 1), (j + 1, -1)]])
        counter = collections.defaultdict(int)
        last = 0
        now = 0
        for ind, delta in tmp:
            counter[now] += ind - last
            last = ind
            now += delta

        nums.sort(reverse=True)
        l = len(nums)
        result = 0
        now = 0
        for count, num in sorted(list(counter.items()), reverse=True):
            result += sum(nums[now: now + num]) * count
            now += num
            if now > l:
                break

        return result % MOD

#         nums.sort(reverse=True)
#         # nums.sort()

#         starts = collections.deque(sorted(i for i, j in requests))
#         ends = collections.deque(sorted(j for i, j in requests))
#         counter = collections.defaultdict(int)
#         now = 0
#         prev = 0
#         while starts or ends:
#             if starts and ends:
#                 if starts[0] > ends[0]:
#                     counter[now] += ends[0] - prev + 1
#                     now -= 1
#                     prev = ends[0] + 1
#                     ends.popleft()
#                 else:
#                     counter[now] += starts[0] - prev
#                     now += 1
#                     prev = starts[0]
#                     starts.popleft()
#             else:
#                 counter[now] += ends[0] - prev + 1
#                 now -= 1
#                 prev = ends[0] + 1
#                 ends.popleft()

#         # counter = collections.defaultdict(int)
#         # for start, end in requests:
#         #     for i in range(start, end + 1):
#         #         counter[i] += 1
#         result = 0
#         now = 0
#         for i in sorted(counter, reverse=True):
#             c = counter[i]
#             result += sum(nums[now: now + c]) * i
#             now += c
#         # for i, j in zip(sorted(counter.values(), reverse=True), nums):
#             # result += i * j
#         return result % (10 ** 9 + 7)
