from sortedcontainers import SortedList

class TimeMap:
    
    def compare(self,a):
        return a[0]

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        
        self.ls = SortedList(key = self.compare)
        self.size = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.ls.add([timestamp,key,value])
        self.size+=1
        

    def get(self, key: str, timestamp: int) -> str:
        
        temp = self.ls.bisect_right([timestamp])
        
        if(temp == 0 or self.size == 0):
            return \"\"
        
        if(temp == self.size or self.ls[temp][0] > timestamp):
            temp-=1
            
        
        while(temp >= 0):
            if(self.ls[temp][1] == key):
                return self.ls[temp][2]
            
            temp-=1
            
        return \"\"
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
