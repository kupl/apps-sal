class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        temp = list(zip(startTime, endTime, profit))
        temp = sorted(temp, key=lambda x: x[0])
        n = len(profit)
        ans = [0 for _ in range(len(profit))]
        ans[-1] = temp[-1][2]

        def binary_s(low, high, end):
            mid = int((low + high) / 2)
            if(mid == high):
                return high
            if(temp[mid][0] < end and temp[mid + 1][0] >= end):
                return mid
            elif(temp[mid][0] >= end):
                return binary_s(low, mid - 1, end)
            else:
                return binary_s(mid + 1, high, end)

        for x in range(n - 2, -1, -1):
            mid = binary_s(x, n - 1, temp[x][1])
            if(mid != n - 1 and temp[mid + 1][0] >= temp[x][1]):
                ans[x] = max(temp[x][2] + ans[mid + 1], ans[x + 1])
            else:
                ans[x] = max(temp[x][2], ans[x + 1])

        return ans[0]
