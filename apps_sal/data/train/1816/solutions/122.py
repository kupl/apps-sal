class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        usage = defaultdict(list)
        for k, name in enumerate(keyName):
            hour, minute = keyTime[k].split(':', 2)
            time_minutes = 60 * int(hour) + int(minute)
            usage[name].append(time_minutes)
        frequent = []
        for name in usage:
            times = sorted(usage[name])
            lo = 0
            hi = 2
            len_times = len(times)
            frequent_name = False
            while hi < len_times and not frequent_name:
                time_span = times[hi] - times[lo]
                if time_span <= 60:
                    frequent.append(name)
                    frequent_name = True
                else:
                    lo += 1
                    hi += 1
        return sorted(frequent)
