class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dix = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dix[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dix or timestamp < self.dix[key][0][0]:
            return \"\"
        
        target = timestamp
        lo = 0
        hi = len(self.dix[key])-1
        
        while lo <hi:
            mid = lo + (hi-lo)//2
            
            if self.dix[key][mid][0] <= target and self.dix[key][mid+1][0] > target:
                return self.dix[key][mid][1]
            
            if  self.dix[key][mid][0] > target:
                hi = mid-1
            else:
                lo = mid+1
        
        return self.dix[key][hi][1] if self.dix[key][hi][0] <= target else self.dix[key][lo][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
