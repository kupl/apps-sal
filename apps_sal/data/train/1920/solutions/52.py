class TimeMap(object):

    def __init__(self):
        self.map = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.map[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        values = self.map[key]
        if not values: return ''
        left, right = 0, len(values) - 1
        while left < right:
            mid = (left + right + 1) // 2
            pre_time, value = values[mid]
            if pre_time > timestamp:
                right = mid - 1
            else:
                left = mid
        return values[left][1] if values[left][0] <= timestamp else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

