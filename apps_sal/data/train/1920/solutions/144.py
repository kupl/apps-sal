class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.kvStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.kvStore:
            values = self.kvStore[key]
            left, right = 0, len(values) - 1

            while left <= right:
                if left == right:
                    return values[left][1]
                
                mid = (left + right) // 2
                midTS, midValue = values[mid]
                
                if midTS == timestamp:
                    return midValue
                elif midTS > timestamp:
                    right = mid - 1
                elif left + 1 <= right and values[left + 1][0] <= timestamp:
                    left = mid + 1
                else:
                    return midValue
                    
        return \"\"
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
