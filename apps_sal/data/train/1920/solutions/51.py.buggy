import bisect
from collections import defaultdict
from dataclasses import dataclass, field

@dataclass(order=True)
class TimeMapValue:
    timestamp: int
    value: Any=field(compare=False)

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort_right(self.map[key], TimeMapValue(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.map[key], TimeMapValue(timestamp, None))
        if i == 0:
            return \"\"
        return \"\" if i == 0 else self.map[key][i - 1].value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
