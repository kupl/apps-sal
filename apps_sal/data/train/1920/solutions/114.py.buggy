import bisect
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.time_map = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
            
    def get(self, key: str, timestamp: int) -> str:
        value_list = self.time_map.get(key, None)
        if not value_list:
            return \"\"
        left, right = 0, len(value_list) - 1
        while left < right:
            mid = (left + right + 1) // 2
            pre_time, value = value_list[mid]
            if pre_time > timestamp:
                right = mid - 1
            else:
                left = mid
        return value_list[left][1] if value_list[left][0] <= timestamp else ''
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
