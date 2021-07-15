class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        from collections import defaultdict
        self.mp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, h = 0, len(self.mp[key])-1
        
        while l <= h:
            mid = (l+h)//2
            if self.mp[key][mid][0] == timestamp:
                return self.mp[key][mid][1]
            elif self.mp[key][mid][0] < timestamp:
                l = mid + 1
            else:
                h = mid - 1
        if h == -1:
            return ''
        else:
            return self.mp[key][h][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
