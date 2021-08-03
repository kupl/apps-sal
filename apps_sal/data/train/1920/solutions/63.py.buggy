class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        items = self.store[key]
        if not items: return ''
        
        left = 0
        right = len(items)
        
        while left < right:
            mid = left + (right-left) // 2
            
            val, prevTime = items[mid]
            
            if items[mid][1] <= timestamp:
                left = mid + 1
            elif items[mid][1] > timestamp:
                right = mid
        
            
        
        return \"\" if right == 0 else items[right - 1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
