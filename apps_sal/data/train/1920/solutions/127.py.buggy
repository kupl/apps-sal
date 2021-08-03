class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        
    def binarySearch(self, l, target):
        low = 0
        high = len(l) - 1
        while low <= high:
            mid = (low + high) // 2
            if l[mid][0] <= target < l[mid + 1][0]:
                return mid
            elif l[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.data or timestamp < self.data[key][0][0]:
            return \"\"
    
        if self.data[key][-1][0] <= timestamp:
            return self.data[key][-1][1]

        return self.data[key][self.binarySearch(self.data[key], timestamp)][1]
