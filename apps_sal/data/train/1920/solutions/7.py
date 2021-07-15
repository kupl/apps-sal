class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.timemap = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        start=0
        end=len(self.timemap[key])-1
        mid=(start+end)//2
        while start<=end:
            if self.timemap[key][mid][1]==timestamp:
                return self.timemap[key][mid][0]
            elif self.timemap[key][mid][1]<timestamp:
                start = mid+1
            elif self.timemap[key][mid][1]>timestamp:
                end=mid-1
            mid = (start+end)//2
        if start>=len(self.timemap[key])-1:
            return self.timemap[key][end][0]
        else:
            return \"\"
        
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
