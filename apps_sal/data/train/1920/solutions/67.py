class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.storage = collections.defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.storage.get(key, '')
        if not lst or lst is None:
            return ''
        #print(lst)
        # The ascii code range of lower char is [97, 122], thus chr(127) can be used to make sure the located index from bisect.bisect(A, (timestamp, chr(127))) can satisfy the condition: timestamp_prev <= timestamp. In fact, chr(ascii_v) can also be used here where ascii_v's range is [123, 127].
        
        idx = bisect.bisect(lst, (timestamp, chr(127)))
        if not idx or idx is None:
            return ''
        
        return lst[idx-1][1]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
