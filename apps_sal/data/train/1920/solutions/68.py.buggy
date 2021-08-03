class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.hash_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hash_map:
            return \"\"
        if self.hash_map[key][0][-1] > timestamp:
            return \"\"
        value_array = self.hash_map[key]
        index = self.binary_search(timestamp, value_array)
        if value_array[index][-1] > timestamp:
            return value_array[index-1][0]
        else:
            return value_array[index][0]
            
        
        
    def binary_search(self, timestamp, value_array):
        left = 0
        right = len(value_array)-1
        while left < right:
            mid = (left+right)//2
            if value_array[mid][-1] < timestamp:
                left = mid+1
            elif value_array[mid][-1] > timestamp:
                right = mid-1
            else:
                return mid
        return left
            
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
