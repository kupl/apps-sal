class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        
        \"\"\"
        self.dic = {}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [[value, timestamp]]
        else:
            self.dic[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.dic or len(self.dic[key]) == 0:
            return \"\"
        
        n = len(self.dic[key])
        
        l = 0
        r = n - 1
        
        while l < r:
            mid = l + (r - l + 1)//2
            if self.dic[key][mid][1] > timestamp:
                r = mid - 1
            elif self.dic[key][mid][1] == timestamp:
                return self.dic[key][mid][0]
            else:
                l = mid
                
        if self.dic[key][l][1] <= timestamp:
            return self.dic[key][l][0]
        else:
            return \"\"
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
