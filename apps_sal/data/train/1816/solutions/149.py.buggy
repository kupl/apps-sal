class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        loginTimes = {}
        workers = set()
        
        def timestamp(time):
            hh, mm = map(int, time.split(\":\"))
            return hh*60 + mm
        
        for name, time in sorted(zip(keyName, keyTime), key=lambda x: (x[1])):
            if name in loginTimes:
                dq = loginTimes[name]
                t = timestamp(time)
                dq.append(t)
                if t - dq[0] > 60:
                    dq.popleft()
                
                if len(dq) >= 3:
                    workers.add(name)
            else:
                loginTimes[name] = deque()
                loginTimes[name].append(timestamp(time))
                
        return sorted(list(workers))
        
        
        
