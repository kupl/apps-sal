class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # need to first sort by time
        pairs = []
        for name, time in zip(keyName, keyTime):
            m, s = time.split(\":\")
            time = 60*int(m) + int(s)
            pairs.append((time, name))
            
        pairs = sorted(pairs)
        usage = defaultdict(list)    
        ret = set()
        for time, name in pairs:
            while usage[name] and usage[name][0] < time-60:
                usage[name].pop(0)
                
            usage[name].append(time)
            
            if len(usage[name]) >= 3:
                # print(name, usage[name])
                ret.add(name)
                
        return sorted(list(ret))
