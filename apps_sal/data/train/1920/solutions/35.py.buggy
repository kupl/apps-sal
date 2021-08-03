class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.values = defaultdict(list)
        self.times = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_right(self.times[key], timestamp)
        return self.values[key][idx-1] if idx else \"\"
    
#      
#     USING BINARY SEARCH
#
#     def get(self, key: str, timestamp: int) -> str:
#         arr = self.map[key]
#         n = len(arr)
        
#         left = 0
#         right = nt
        
#         while left < right:
#             mid = (left + right) // 2
            
#             if arr[mid][0] <= timestamp:
#                 left = mid + 1
#             elif arr[mid][0] > timestamp:
#                 right = mid
                
#         return arr[right-1][1] if (right > 0) else \"\"


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# kv.set(\"love\", \"high\", 10); 
# kv.set(\"love\", \"low\", 20); 
# kv.get(\"love\", 5); -> \"\"
# kv.get(\"love\", 10); -> high
# kv.get(\"love\", 15); -> high
# kv.get(\"love\", 20); -> low
# kv.get(\"love\", 25); -> low


