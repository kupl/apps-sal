from collections import deque
class TimeMap:

    def bs(self, target, seq):
        low = 0
        high = len(seq) - 1
        result = ''
        foundTs = -1
        while(low <= high):
            mid = (low + high) // 2
            ts = seq[mid][0]
            if ts <= target:
                if ts == target:
                    return seq[mid][1]
                elif ts > foundTs:
                    foundTs = ts
                    result = seq[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return result
                
    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = {}    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ''
        return self.bs(timestamp, self.map[key])


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
