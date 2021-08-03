class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.M = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # A = self.M.get(key, None)
        # if not A:
        #     return \"\"
        # i = bisect.bisect_right(A, (timestamp,))
        # if i == 0:
        #     return \"\"
        # else:
        #     return A[i-1][1]
        
        lo,hi = 0, len(self.M[key]) - 1
        while(lo < hi):
            med = (lo + hi + 1) // 2
            if self.M[key][med][0] <= timestamp: lo = med
            else: hi = med - 1
        return self.M[key][lo][1] if lo < len(self.M[key]) and self.M[key][lo][0] <= timestamp else ''
    
        # while lo < hi:
        #     mid = (lo + hi + 1) // 2 #why + 1?
        #     if self.M[key][mid][0] <= timestamp: 
        #         lo = mid + 1
        #     else: hi = mid
        # ind = lo - 1
        # if ind < len(self.M[key]) and self.M[key][ind][0] <= timestamp:
        #     # why < len?
        #     return self.M[key][lo - 1][1]
        # else:
        #     return ''
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
