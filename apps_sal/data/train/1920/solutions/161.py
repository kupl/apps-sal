class TimeMap:

    def __init__(self):
        self._data = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self._data[key].append((value, timestamp))

    def get(self, key, timestamp):
        if key not in self._data:
            return ''

        arr = self._data[key]
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid][1] <= timestamp:
                start = mid
            else:
                end = mid - 1

        if arr[end][1] <= timestamp:
            return arr[end][0]
        if arr[start][1] <= timestamp:
            return arr[start][0]

        return ''
