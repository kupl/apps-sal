def debug(s, *args):
    pass
    # prin/t(s, args)


class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        debug('set', key, value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        debug('get', key, timestamp)
        vals = self.d[key]
        if not vals:
            return \"\"
        
        # Binary search the right value
        lo, hi = 0, len(vals)-1
        
        idx = None
        debug('binsearch', vals, timestamp)
        while lo <= hi:
            mid = (lo+hi)//2
            debug('#', lo, hi, mid)
            
            if timestamp >= vals[mid][0] and (mid+1 == len(vals) or timestamp < vals[mid+1][0]):
                idx = mid
                break
            
            if timestamp > vals[mid][0]:
                lo = mid + 1
            else:
                hi = mid - 1

        debug('idx', idx)
        if idx != None:
            return vals[idx][1]
        return \"\"
    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
