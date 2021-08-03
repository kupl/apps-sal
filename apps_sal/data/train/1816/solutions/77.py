class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def timeDifference(time1, time2):
            hr1, min1 = time1.split(':')
            hr2, min2 = time2.split(':')
            timeDiff = (int(hr2) - int(hr1)) * 60 + int(min2) - int(min1)
            return timeDiff

        res = set()
        rec = collections.defaultdict(list)
        N = len(keyName)
        for i in range(N):
            hr, minute = keyTime[i].split(':')
            time = int(hr) * 60 + int(minute)
            rec[keyName[i]].append(time)
        for key, val in list(rec.items()):
            if len(val) >= 3:
                sorted_time = sorted(val)
                for i in range(2, len(val)):
                    if sorted_time[i] - sorted_time[i - 2] <= 60:
                        res.add(key)
                        break
        return sorted(list(res))
