class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append( (timestamp, value) )
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ''
        
        stack = self.d[key]
        
        idx = bisect.bisect(stack, (timestamp, chr(123)) )
        
        return stack[idx - 1][1] if idx else ''
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

#use binary search  

#List((timestamp: dict))
