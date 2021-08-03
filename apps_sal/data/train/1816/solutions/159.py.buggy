class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def toTime(hhmm):
            hh, mm = hhmm.split(\":\")
            return int(hh) * 60 + int(mm)
        
        res = set()
        mq = collections.defaultdict(collections.deque)
        for name, time in sorted(zip(keyName, keyTime), key=lambda x: x[1]):
            # print(name, time)
            t = toTime(time)
            q = mq[name]
            while len(q) > 0 and q[0] < t - 60:
                q.popleft()
            q.append(t)
            
            # print(q)
            if len(q) >= 3:
                res.add(name)
        
        return sorted(list(res))
