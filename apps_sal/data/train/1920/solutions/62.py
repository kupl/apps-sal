from collections import defaultdict
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = defaultdict(list) # key -> (value, timestamp)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps are strictly increasing so don't worry about key being in it alreadu
        self.store[key] += [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        # here we can do a binary search to find the greatest timestamp less than timestamp
        if not self.store[key] or timestamp < self.store[key][0][1]:
            return \"\"
        
        # binary search template 1, whilst returning smaller one (r) if we don't find
        lst = self.store[key]
        l, r = 0, len(lst)-1
        while l <= r:
            m = l + (r-l)//2
            if lst[m][1] == timestamp:
                return lst[m][0]
            
            elif timestamp > lst[m][1]:
                l = m + 1
            else:
                r = m - 1
        return lst[r][0]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
