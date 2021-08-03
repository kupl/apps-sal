class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        startTime = [i - queryTime for i in startTime]
        endTime = [i - queryTime for i in endTime]

        count = 0

        for i, j in zip(startTime, endTime):
            if (i <= 0) & (j >= 0):
                count += 1

        return count
