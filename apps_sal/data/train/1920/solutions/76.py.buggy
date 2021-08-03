class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map=collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.map[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.map or self.map[key][0][1]>timestamp:
            
            return \"\"
        
        v=self.map[key]
        
        l, r=0,len(v)
        
        while l<r:
            
            mid=(l+r)//2
            
            if v[mid][1]==timestamp:
                return v[mid][0]
            
            if v[mid][1]>timestamp:
                r=mid
                
            else:
                l=mid+1
        
    
        return v[r-1][0] 
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
