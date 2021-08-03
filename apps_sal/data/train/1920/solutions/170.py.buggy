class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.key_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.key_map.get(key):
            self.key_map[key] = []
        self.key_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val = \"\"
        timestamp_list = self.key_map.get(key)
        if timestamp_list:
            index = bisect.bisect(timestamp_list, (timestamp,))
            # print (timestamp, index)
            # print (timestamp_list)
            if index > len(timestamp_list) - 1:
                index -= 1
            
            if timestamp_list[index][0] > timestamp:
                index -= 1

            if index >= 0:
                val = timestamp_list[index][1]
        return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
