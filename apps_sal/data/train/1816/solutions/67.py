from collections import defaultdict


def mins_since_midnight(str_time):
    hours = int(str_time[:2])
    mins = int(str_time[3:])
    return hours * 60 + mins


def difference_mins(str_time1, str_time2):
    return abs(mins_since_midnight(str_time2) - mins_since_midnight(str_time1))


class Solution:
    def alertNames(self, keyName, keyTime):
        alert_names = []
        log = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            log[name].append(time)

        for name in log.keys():
            times = log[name]
            sorted_times = sorted(times)
            start = 0
            n = 1
            for i in range(1, len(sorted_times)):
                n += 1
                if difference_mins(sorted_times[start], sorted_times[i]) <= 60:
                    if n == 3:
                        alert_names.append(name)
                        break
                else:
                    while difference_mins(sorted_times[start], sorted_times[i]) > 60:
                        start += 1
                        n -= 1

        return sorted(alert_names)
