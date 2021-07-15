class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def convert_to_minutes(time):
            hhmm = time.split(':')
            hh, mm = int(hhmm[0]), int(hhmm[1])
            return 60*hh + mm
        
        mod = 24*60
        res = set()
        minutes = [convert_to_minutes(hhmm) for hhmm in keyTime]
        d = collections.defaultdict(list)
        for i in range(len(minutes)):
            worker = keyName[i]
            time = minutes[i]
            d[worker].append(time)
        for worker in d:
            d[worker].sort()
            for i in range(2, len(d[worker])):
                if d[worker][i] - d[worker][i-2] <= 60:
                    res.add(worker)
                    break
        return sorted(list(res))
