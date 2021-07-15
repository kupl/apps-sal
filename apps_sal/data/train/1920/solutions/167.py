class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        left = 0
        right = len(self.dict[key])
        
        while left < right:
            mid = (left+right)//2
            
            if self.dict[key][mid][0] == timestamp:
                return self.dict[key][mid][1]
            elif self.dict[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
            
        return \"\" if right == 0 else self.dict[key][right-1][1]
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
