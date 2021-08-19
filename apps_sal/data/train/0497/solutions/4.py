class Solution:

    def binSearch(self, stack: List[int], target: int) -> List[int]:
        left = 0
        right = len(stack) - 1
        while left <= right:
            mid = (left + right + 1) // 2
            if stack[mid][1] > target:
                right = mid - 1
            elif stack[mid][1] == target or (left == right and stack[mid][1] < target):
                return stack[mid]
            else:
                left = mid
        return None

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        stack = []
        for i in range(n):
            job = jobs[i]
            prev = self.binSearch(stack, job[0])
            if prev is not None:
                job[2] += prev[2]
            if not stack or stack[-1][2] < job[2]:
                stack.append(job)
        return stack[-1][2]
