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
        val_index = -1
        for i in range(len(all_values)-1, -1, -1):
            if all_values[i][0] <= timestamp:
                val_index = i
                break
        return all_values[val_index][1] if val_index > -1 else \"\"
            
                
    
