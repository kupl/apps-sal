class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l = self.hashmap[key]
        
        left = 0
        right = len(l)-1 
        
        if l[0][1] > timestamp:
            return \"\"
        
        while left <= right:
            mid = left + (right-left) // 2 
            if l[mid][1] <= timestamp:
                left = mid+1 
            else:
                right = mid-1
        return l[right][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
