class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([timestamp, value])        

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        
        left = 0
        right = len(values)
        
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            elif values[mid][0] > timestamp:
                right = mid
        
        return \"\" if right == 0 else values[right - 1][1]


