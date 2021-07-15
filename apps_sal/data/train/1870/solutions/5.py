class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = len(count)
        maximum = 0
        sumValues = 0
        for i, value in enumerate(count):
            if value != 0:
                minimum = min(i, minimum)
                maximum = max(i, maximum)
                sumValues += i * value
            if value == max(count):
                mode = i
                
        mean = sumValues / sum(count)
        
        if len(count) % 2 == 0:
            lowMid = sum(count) // 2
            upMid = lowMid + 1
            currentCount = 0
            median = 0
            for i, e in enumerate(count):
                currentCount += e
                if currentCount >= lowMid and median == 0:
                    median += i / 2
                if currentCount >= upMid:
                    median += i / 2
                    break
        else:
            mid = (sum(count) // 2) + 1
            currentCount = 0
            median = 0
            for i, e in enumerate(count):
                currentCount += e
                if currentCount >= mid:
                    median += i
                    break
        
        return [minimum, maximum,  mean, median, mode]

