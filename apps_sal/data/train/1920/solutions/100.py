class TimeMap:
    from collections import defaultdict
    import bisect
    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        sorted_timestamp = self.timemap[key]
        sorted_timestamp.insert( bisect.bisect_right(sorted_timestamp, (timestamp, value)), (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        sorted_timestamp = self.timemap[key]
        index = bisect.bisect_left(sorted_timestamp, (timestamp, ''))
        if index == len(sorted_timestamp):
            return sorted_timestamp[-1][1]
        elif sorted_timestamp[index][0] == timestamp:
            return sorted_timestamp[index][1]
        elif index == 0 and sorted_timestamp[index][0] != timestamp:
            return ''
        else:
            return sorted_timestamp[index-1][1]
