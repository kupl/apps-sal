class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        
        for i, j in zip(startTime, endTime):
            if (i <= queryTime) & (j >= queryTime):
                count += 1
                
        return count
