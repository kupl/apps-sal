class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        # save a hashmap of key => [... (value, timestamp) ...]
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return \"\"
        else:
            # now do bst
            left = 0
            right = len(self.store[key]) - 1
            while left <= right:
                mid = (left + right) // 2
                if self.store[key][mid][1] <= timestamp:
                    # ensure that it is the largest
                    next_left = mid + 1
                    next_mid = (next_left + right) // 2
                    if next_left > right or self.store[key][next_mid][1] > timestamp:
                        return self.store[key][mid][0]
                    left = next_left
                else:
                    right = mid - 1
            return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
