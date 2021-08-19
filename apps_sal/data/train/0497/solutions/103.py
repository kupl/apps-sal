class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        #         def binary_search(intervals, index):

        #             start = 0
        #             end = index - 1

        #             while start <= end:
        #                 mid = (start + end) // 2

        #                 if intervals[index][0] < intervals[mid][1]:
        #                     end = mid - 1
        #                 else:
        #                     start = mid + 1

        #             return start - 1

        def binary_search(intervals, index):

            start = 0
            end = index

            while start < end:
                mid = (start + end) // 2

                if intervals[mid][1] > intervals[index][0]:
                    end = mid
                else:
                    start = mid + 1

            return start - 1

        intervals = []
        for i in range(len(startTime)):
            intervals.append((startTime[i], endTime[i], profit[i]))

        intervals.sort(key=lambda i: i[1])
        # print(intervals)
        # see other submitted code for clear explanation
        dp = [0] * len(intervals)
        for i in range(len(intervals)):
            profit_if_i_inlcuded = intervals[i][2]

            k_th = binary_search(intervals, i)

            if (k_th != -1):
                profit_if_i_inlcuded += dp[k_th]

            dp[i] = max(dp[i - 1], profit_if_i_inlcuded)  # max of not including i, including i
            # print(intervals, i, k_th, dp)
        return max(dp)

    # almost all  test cases passed
#     def jobScheduling_n2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

#         def binary_search(intervals, index):

#             start = 0
#             end = index - 1

#             while start <= end:
#                 mid = (start + end) // 2

#                 if intervals[index][0] < intervals[mid][1]:
#                     end = mid - 1
#                 else:
#                     start = mid + 1

#             return start - 1

#         intervals = []
#         for i in range(len(startTime)):
#             intervals.append((startTime[i], endTime[i], profit[i]))

#         intervals.sort(key=lambda i: i[1])
#         # print(intervals)
#         dp = [0] * len(intervals)
#         for i in range(len(intervals)):
#             dp[i] = intervals[i][2]

#             k_th = binary_search(intervals, i)

#             if k_th != -1:
#                 for j in range(0, k_th + 1):
#                     if dp[i] < dp[j] + intervals[i][2]:
#                         dp[i] = dp[j] + intervals[i][2]

#         # print(dp)
#         return max(dp)

#     def jobScheduling_n2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

#         intervals = []
#         for i in range(len(startTime)):
#             intervals.append((startTime[i], endTime[i], profit[i]))

#         intervals.sort(key=lambda i: i[1])
#         # print(intervals)
#         dp = [0] * len(intervals)
#         for i in range(len(intervals)):
#             dp[i] = intervals[i][2]

#             for j in range(0, i):

#                 if intervals[i][0] >= intervals[j][1]:
#                     if dp[i] < dp[j] + intervals[i][2]:
#                         dp[i] = dp[j] + intervals[i][2]

#         # print(dp)
#         return max(dp)
