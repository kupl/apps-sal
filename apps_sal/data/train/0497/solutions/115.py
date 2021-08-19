class Solution:

    def next_index(self, arr, i, target):

        left = 0
        right = i

        if i < 0:
            return -1

        mid = left
        while left < right:

            mid = (left + right + 1) // 2
            # print(left,mid,right)
            if arr[mid][1] <= target:
                left = mid
            elif arr[mid][1] > target:
                right = mid - 1

        return left if arr[left][1] <= target else -1

    def solve(self, i, arr):

        if i < 0:
            return 0

        if i in self.dp:
            return self.dp[i]

        x = self.solve(i - 1, arr)

        y = 0
        ind = self.next_index(arr, i - 1, arr[i][0])

        y = self.solve(ind, arr) + arr[i][2]

        self.dp[i] = max(x, y)

        return self.dp[i]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        self.dp = {}

        arr = []

        for i in range(len(startTime)):

            arr.append((startTime[i], endTime[i], profit[i]))

        arr.sort(key=lambda x: x[1])

        # print(arr)

        ans = self.solve(len(profit) - 1, arr)

        # print(self.dp)

        # print(self.next_index(arr,2,2))
        return ans
