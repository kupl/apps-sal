class Solution:

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for (idx, x) in enumerate(startTime):
            if x <= queryTime <= endTime[idx]:
                count += 1
        return count
