class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.dic[key].append([timestamp,value])
        
    def get(self, key: str, timestamp: int) -> str:
        
        left = 0
        right = len(self.dic[key]) - 1
        
        if self.dic[key][left][0] > timestamp:
            return ''
        while left < right:
            mid = left + (right-left+1) // 2
            if self.dic[key][mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid
                
        return self.dic[key][left][1]
        
        
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
