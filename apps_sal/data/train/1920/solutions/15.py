class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.M = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str: 
        lo,hi = 0, len(self.M[key]) 
        while(lo < hi):
            med = lo+(hi-lo)// 2
            if self.M[key][med][0] <= timestamp: lo = med+1
            else: hi = med
        return self.M[key][lo-1][1] 
    # lo-1<len(self.M[key]) # 

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.M = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str: 
        lo,hi = 0, len(self.M[key]) - 1
        while(lo < hi):
            med = (lo + hi + 1) // 2
            if self.M[key][med][0] <= timestamp: lo = med
            else: hi = med - 1
        return self.M[key][lo][1] if lo < len(self.M[key]) and self.M[key][lo][0] <= timestamp else ''
            
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
