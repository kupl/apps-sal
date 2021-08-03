from collections import defaultdict
from collections import deque


class Solution:
    def alertNames(self, key_name, key_time):
        time_name = []
        for name, time_ in zip(key_name, key_time):
            hour_str, minute_str = time_.split(':')
            hour, minute = int(hour_str), int(minute_str)
            time_name.append((60 * hour + minute, name))
        time_name.sort()

        mapping = defaultdict(deque)
        res = set()
        for time_, name in time_name:
            curr = mapping[name]
            while curr and time_ - curr[0] > 60:
                curr.popleft()
            curr.append(time_)
            if len(curr) >= 3:
                res.add(name)

        return sorted(res)
