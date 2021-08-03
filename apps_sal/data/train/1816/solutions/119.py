import bisect


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = {}
        for i in range(len(keyName)):
            name = keyName[i]
            time = keyTime[i].split(':')
            time = int(time[0]) * 60 + int(time[1])
            if name not in d:
                d[name] = []
                pass
            bisect.insort_left(d[name], time)
            pass
        ret = set()
        for name in d:
            lst = d[name]
            window = []
            for time in lst:
                now = time
                hour = now - 60
                while len(window) > 0 and window[0] < hour:
                    del window[0]
                    pass
                window.append(now)
                if len(window) >= 3:
                    ret.add(name)
                    pass
                pass
            pass
        return list(sorted(ret))
