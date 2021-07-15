class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        all_values = self.dic[key]
        if not all_values:
            return \"\"
        val = \"\"
        left = 0
        right = len(all_values) -1
        while left <= right:
            middle = (left + right) // 2
            if all_values[middle][0] == timestamp:
                val = all_values[middle][1]
                break
            elif all_values[middle][0] < timestamp:
                val = all_values[middle][1]
                left = middle + 1
            else:
                right = middle - 1
                
        return val
                
    
