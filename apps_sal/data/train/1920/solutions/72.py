class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map.setdefault(key, [])
        self.map[key].append((value, timestamp))

    def binarySearch(self, arr, target, start, end):
        midpoint = (start + end) // 2
        if arr[midpoint][1] == target:
            return arr[midpoint][0]
        
        if arr[midpoint][1] < target:
            if midpoint + 1 > end or arr[midpoint][1] > target:
                return arr[midpoint][0]
            return self.binarySearch(arr, target, midpoint+1, end)
        else:
            return self.binarySearch(arr, target, start, midpoint-1)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or timestamp < self.map[key][0][1]:
            return \"\"
            
        return self.binarySearch(self.map[key], timestamp, 0, len(self.map[key])-1)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
