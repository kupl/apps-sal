from collections import defaultdict
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        insert_index = self.__binary_search(self.map[key], timestamp) + 1
        self.map[key].insert(insert_index, (value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        search_index = self.__binary_search(self.map[key], timestamp)
        if search_index == -1:
            return \"\"
        return self.map[key][search_index][0]
    
    def __binary_search(self, collection, timestamp):
        n = len(collection)
        lo, hi = 0, n-1
         
        while lo <= hi:
            mid = (lo+hi) // 2
            if mid == n-1:
                return n-1
            elif collection[mid][1] <= timestamp < collection[mid+1][1]:
                return mid
            elif collection[mid+1][1] <= timestamp:
                lo = mid + 1
            elif collection[mid][1] > timestamp:
                hi = mid - 1
        
        return -1
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
