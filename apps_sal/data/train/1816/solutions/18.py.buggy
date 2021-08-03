class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        m = {}
        N = len(keyName)
        alerts = set()
        minutes = lambda time:int(time.split(\":\")[0])*60 + int(time.split(\":\")[1])
        for name, time in zip(keyName, keyTime):
            if name not in m:
                m[name] = collections.deque()
            m[name].append(minutes(time))
        
        for name, times in m.items():
            q = collections.deque()
            for time in sorted(times):
                while len(q) and q[0]+60 < time:
                    q.popleft()
                q.append(time)
                if(len(q)>2):
                    alerts.add(name)
                    break
        return sorted(alerts)
            
