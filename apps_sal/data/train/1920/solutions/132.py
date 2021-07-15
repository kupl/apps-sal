class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = {'times':[],'values':[]}
        self.hash[key]['values'].append(value)
        self.hash[key]['times'].append(timestamp)
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return \"\"
        
        values = self.hash[key]['times']
        idx = search(timestamp,self.hash[key]['times'])
        # print(\"This is the key:\",key)
        # print(\"This is the values:\",self.hash[key]['values'])
        # print(\"This is times:\",values)
        # print(\"This is timestamp:\",timestamp)
        # print(\"This is idx:\",idx)
        # print(\"*******************\")
        if idx is not None:
            return self.hash[key]['values'][idx]
        return \"\"
        
        
def search(target,values):
    l = 0
    r = len(values)-1
    ans = None
    
    while l<=r:
        mid = (l+r)//2
        
        if values[mid]==target:
            return mid
        
        if values[mid]>target:
            r = mid-1
        
        if values[mid]<target:
            ans = mid
            l = mid+1
    
    return ans
        
    
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
