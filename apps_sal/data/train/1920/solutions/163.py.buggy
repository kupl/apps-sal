class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.memo = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self.memo.get(key, None):
            lst = self.memo[key]

            left = 0
            right = len(lst) - 1
            while left <= right:
                mid = (left + right) // 2
                if lst[mid][0] <= timestamp and (mid == len(lst) - 1 or lst[mid+1][0] > timestamp):
                    return lst[mid][1]
                elif lst[mid][0] > timestamp:
                    right = mid -1
                elif lst[mid+1][0] <= timestamp:
                    left = mid + 1
            return \"\"
        else:
            return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
