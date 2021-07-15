class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def should_alert(t):
            if len(t) < 3:
                return False
            
            for i in range(len(t) - 2):
                if t[i + 2] <= t[i] + 100:
                    return True
            return False
        
        time = collections.defaultdict(list)
        alert = []
        for name, t in zip(keyName, keyTime):            
            ti = int(t[:2] + t[3:])
            time[name].append(ti)
        
        ret = []
        for name in time:
            time[name].sort()
            if should_alert(time[name]):
                ret.append(name)
    
        ret.sort()
        return ret
