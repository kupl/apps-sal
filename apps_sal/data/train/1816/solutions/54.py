class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def getmins(time):
            h, m = time.split(':')
            return int(h) * 60 + int(m)

        def timediff(time1, time2):
            return getmins(time1) - getmins(time2)
        d = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            d[name].append(time)
        res = []
        for key in d:
            vals = d[key]
            slow = 0
            for fast in range(len(vals)):
                vals.sort()
                while timediff(vals[fast], vals[slow]) > 60:
                    slow += 1
                if fast - slow >= 2:
                    res.append(key)
                    break
        res.sort()
        return res
