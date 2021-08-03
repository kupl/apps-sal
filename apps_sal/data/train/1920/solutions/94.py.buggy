class TimeMap():

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.timeMap = collections.defaultdict(deque)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
          
        self.timeMap[key].appendleft((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timeMap:
            return(\"\")
        
        curr = \"\"

        for val, time in self.timeMap[key]:
            
            if time <= timestamp:
                return(val)
                   
        return(curr)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
