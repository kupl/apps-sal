class Solution:
    def alertNames(self, keyName, keyTime):
        from collections import defaultdict
        import datetime
        d = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            d[name].append(time)

        ans = set()
        for key in d:
            d[key].sort()

            for i in range(len(d[key]) - 2):
                time1, time2 = d[key][i], d[key][i + 2]
                FMT = '%H:%M'
                dt1 = datetime.datetime.strptime(time1, FMT)
                dt2 = datetime.datetime.strptime(time2, FMT)
                diff = dt2 - dt1
                if diff.total_seconds() <= 3600:
                    ans.add(key)

        return sorted(list(ans))
