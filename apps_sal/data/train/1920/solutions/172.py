class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data: return \"\"  
        lo = 0
        hi = len(self.data[key])
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.data[key][mid][1] == timestamp:
                return self.data[key][mid][0]
            elif self.data[key][mid][1] < timestamp:
                lo = mid + 1
            else: 
                hi = mid
        
        if lo == 0 and self.data[key][lo][1] > timestamp:
            return \"\"
        return self.data[key][lo-1][0]
        
        

