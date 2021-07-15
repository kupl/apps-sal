class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        # key is str, value is a list of list sorted by timestamp in increasing order
        self.records = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.records:
            self.records[key] = [[timestamp, value]]
        else:
            self.records[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ''
        to_search = self.records[key]
        val = self.b_search(timestamp, to_search)
        return val
        
    def b_search(self, target, array):
        start, end = 0, len(array)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if array[mid][0] == target:
                return array[mid][1]
            elif array[mid][0] < target:
                start = mid
            else:
                end = mid - 1
        if array[end][0] <= target:
            return array[end][1]
        if array[start][0] <= target:
            return array[start][1]
        return \"\"
        
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
