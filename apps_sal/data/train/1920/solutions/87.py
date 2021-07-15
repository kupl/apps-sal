class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dic = dict() 
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return \"\"
        left = 0
        right = len(self.dic[key])
        mid = None
        while left < right:
            mid = (left + right)//2
            if self.dic[key][mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1
        return \"\" if right==0 else self.dic[key][right-1][1]
