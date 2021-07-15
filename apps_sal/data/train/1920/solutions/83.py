from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\" Initialize your data structure here. \"\"\"
        self.TimeMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].insert(0, (value, timestamp))
        # print(self.TimeMap)
        
    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.TimeMap:
            temp_list = self.TimeMap[key]
            for item in temp_list:
                value, timestamp_prev = item[0], item[1]
                if timestamp_prev <= timestamp:
                    return value
            
            return \"\"

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
