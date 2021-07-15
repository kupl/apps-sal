class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.values = defaultdict(list)  # key = [(timestamp, value), (timestamp, value)]


    def set(self, key: str, value: str, timestamp: int) -> None:
        print(f'set({key}, {timestamp}, {value})')
        self.values[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # we need to look through self.values[key] to find the value time closest to timestamp without
        # going over.
        values = self.values[key]

        # binary search. if the mid time is greater than timestamp, start with the left half.
        left = 0
        right = len(values) - 1
        found = None

        #print(f'get({key}, {timestamp}) initial found={found} left={left} right={right}')
        while right >= left:
            mid = left + (right - left) // 2
            #print(f'  top left={left} right={right} mid={mid}')
            if timestamp < values[mid][0]:
                right = mid - 1
                #print(f'    timestamp {timestamp} is under {values[mid][0]}, taking left side, found={found} left={left} right={right}')
            elif timestamp > values[mid][0]:
                found = mid
                left = mid + 1
                #print(f'    timestamp {timestamp} is over {values[mid][0]}, taking right side, found={found} left={left} right={right}')
            else:
                #print(f'    timestamp is a match, found={found}')
                found = mid
                break
                
        if found is None:
            return ''
        
        #print(f'  returning {values[found][1]}')
        return values[found][1]
            
            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# n = 3

# 1 2 3 4
