class TimeMap:
    def __init__(self):
        self.lookup = {}

    def set(self, key, value, timestamp):
        if key not in self.lookup:
            self.lookup[key] = [[timestamp, value]]
        else:
            self.lookup[key].append([timestamp, value])

    def get(self, key, timestamp):
        if key not in self.lookup:
            return \"\"

        values = self.lookup[key]

        # timestamp is asking for something earlier than our first timestamp
        if values[0][0] > timestamp:
            return \"\"
        # timestamp is asking for something later than our last timestamp
        elif values[-1][0] <= timestamp:
            return values[-1][1]

        left = 0
        right = len(values)
        while left <= right:
            # prevents sum overflow
            mid = left + (right-left)//2

            if values[mid][0] == timestamp:
                return values[mid][1]

            if values[mid][0] < timestamp:
                left = mid + 1
            elif values[mid][0] > timestamp:
                right = mid - 1

        # could not find, so return one before l == r
        return values[right][1]

