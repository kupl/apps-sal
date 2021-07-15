class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        m = collections.defaultdict(list)
        for i in range(len(keyName)):
            tokens = keyTime[i].split(':')
            hour, minute = int(tokens[0]), int(tokens[1])
            ts = hour * 60 + minute
            m[keyName[i]].append(ts)
            
        for k in m:
            m[k].sort()
        
        ts_by_name = collections.defaultdict(list)
        offenders = set()
        for name in m:
            for ts in m[name]:
                while len(ts_by_name[name]) > 0 and (ts_by_name[name][0] > ts or ts - ts_by_name[name][0] > 60):
                    ts_by_name[name].pop(0)
                        
                ts_by_name[name].append(ts)
                if len(ts_by_name[name]) == 3:
                    offenders.add(name)
                
        return sorted(list(offenders))
