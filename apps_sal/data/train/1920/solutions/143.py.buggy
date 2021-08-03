class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        # next((v for v,t in reversed(self.d[key]) if t <= timestamp), \"\")
        return self.bsearch(self.d[key], timestamp)
    
    def bsearch(self, l, time):
        if not l:
            return \"\"

        lo, hi = 0, len(l)-1
        while lo <= hi:
            mid = (hi+lo)//2
            v, t = l[mid]
            if t <= time:
                lo = mid + 1 
            else:
                hi = mid - 1
                
        return l[hi][0] if l[hi][1] <= time else \"\"
            
            
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
