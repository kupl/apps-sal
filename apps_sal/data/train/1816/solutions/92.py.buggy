class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def _listify_time(time):
            time = time.split(\":\")
            return [int(x) for x in time]
        
        def _time_diff(time1, time2):
            time1 = _listify_time(time1)
            time2 = _listify_time(time2)
            return 60 * (time2[0] - time1[0]) + time2[1] - time1[1]
        
        both = [(keyTime[i], keyName[i]) for i in range(len(keyTime))]
        both.sort(key = lambda l: _time_diff(\"00:00\", l[0]))
        keyTime = [l[0] for l in both]
        keyName = [l[1] for l in both]
        
        times = collections.defaultdict(list)
        res = []
        
        for i in range(len(keyName)):
            
            times[keyName[i]].append(keyTime[i])
            if len(times[keyName[i]]) >= 3:
                if _time_diff(times[keyName[i]][-3], times[keyName[i]][-1]) <= 60:
                    res.append(keyName[i])
        
        res = sorted(list(set(res)))
        return res
