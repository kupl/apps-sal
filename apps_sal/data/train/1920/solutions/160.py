from heapq import heappop, heappush
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.res={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.res:
            self.res[key]=[]
            self.res[key]=[[value,timestamp]]
        else:
             self.res[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        array=self.res[key]
        n = len(self.res[key])
        i = 0
        j =n-1
        if array[i][1]>timestamp:
            return \"\"
        while i<=j:
            mid = i+(j-i)//2
            if array[mid][1]==timestamp:
                return array[mid][0]
            elif array[mid][1]<timestamp:
                i = mid+1
            else:
                j = mid-1
        return array[j][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
