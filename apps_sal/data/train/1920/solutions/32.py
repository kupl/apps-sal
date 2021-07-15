class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self._dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._dict:
            self._dict[key] = [(value, timestamp)]
        else:
            val_time_list = self._dict[key]
            i, j = 0, len(val_time_list) - 1
            pos = 0
            while i <= j:
                mid = (i + j) // 2
                if val_time_list[mid][1] == timestamp:
                    pos = mid
                    break
                if val_time_list[mid][1] > timestamp:
                    j = mid - 1
                else:
                    i = mid + 1
            pos = j + 1
            val_time_list.insert(pos, (value, timestamp))
            self._dict[key] = val_time_list
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._dict:
            return ''
        val_time_list = self._dict[key]
        i, j = 0, len(val_time_list) - 1
        pos = 0
        while i <= j:
            mid = (i + j) // 2
            if val_time_list[mid][1] == timestamp:
                return val_time_list[mid][0]
            if val_time_list[mid][1] > timestamp:
                j = mid - 1
            else:
                i = mid + 1
        if j >= 0: return val_time_list[j][0]
        else: return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
