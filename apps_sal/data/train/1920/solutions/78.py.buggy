class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.timeStamp = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStamp:
            self.timeStamp[key] = {'values':[],'time':[]}
        self.timeStamp[key]['values'].append(value)
        self.timeStamp[key]['time'].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        times = self.timeStamp[key]['time']
        
        idx = binarySearch(times,timestamp)
        
        if idx == 0:
            return \"\"
        
        return self.timeStamp[key]['values'][idx-1]


def binarySearch(times,key):
    l = 0
    h = len(times)
    
    while (l<h):
        mid = (l+h)//2
        
        if times[mid]<=key:
            l = mid+1
        elif times[mid]>key:
            h = mid
    
    return h


# def get(self, key, timestamp):
#         arr = self.dic[key]
#         n = len(arr)
        
#         left = 0
#         right = n
        
#         while left < right:
#             mid = (left + right) / 2
#             if arr[mid][0] <= timestamp:
#                 left = mid + 1
#             elif arr[mid][0] > timestamp:
#                 right = mid
        
#         return \"\" if right == 0 else arr[right - 1][1]
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
