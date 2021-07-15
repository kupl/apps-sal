class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key]:
            return \"\"
        if len(self.d[key]) == 1:
            if self.d[key][0][1] <= timestamp:
                return self.d[key][0][0]
            else:
                return \"\"
        
        i=0
        j=len(self.d[key])-1
        while i<=j:
            m=i + ((j-i)//2)
            if self.d[key][m][1]<timestamp:
                i=m+1
            elif self.d[key][m][1]>timestamp:
                j=m-1
            elif self.d[key][m][1]==timestamp:
                return self.d[key][m][0]
            else:
                pass
        if j!=-1:
            return self.d[key][j][0]
        else:
            return \"\"
            
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
