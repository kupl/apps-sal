class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)
        slots = []
        for i in range(n):
            slots.append([startTime[i], endTime[i], profit[i]])

        slots.sort(key=lambda x: (x[0], x[1]))
        mem = {}

        def dp(i):
            if i >= n:
                return 0
            if i == n - 1:
                mem[i] = slots[i][2]
                return mem[i]

            if i in mem:
                return mem[i]
            max_non_overlapping_val = slots[i][2]

            for j in range(i + 1, n):
                if slots[j][0] < slots[i][1]:
                    continue

                max_non_overlapping_val = max(max_non_overlapping_val, slots[i][2] + dp(j))
                break

            max_non_overlapping_val = max(max_non_overlapping_val, dp(i + 1))
            mem[i] = max_non_overlapping_val
            return mem[i]

        return dp(0)
