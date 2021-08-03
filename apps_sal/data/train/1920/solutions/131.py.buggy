class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        sorted_values = self.store.get(key, None)
        if sorted_values is None: return \"\"
        value = self.bisect_with_timestamp(0, len(sorted_values) - 1, sorted_values, timestamp)
        return value
        
    def bisect_with_timestamp(self, left, right, values, timestamp):
        while left <= right:
            pivot = (left + right) // 2
            pivot_stamp, pivot_value = values[pivot]
            if pivot_stamp == timestamp:
                return pivot_value
            else:
                if pivot_stamp < timestamp:
                    left = pivot + 1
                else:
                    right = pivot - 1
                    
        pivot_stamp, pivot_value = values[pivot]
        if pivot_stamp < timestamp:
            return pivot_value
        else:
            if pivot - 1 >= 0:
                pivot_stamp, pivot_value = values[pivot - 1]
                return pivot_value
            else:
                return \"\"
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
