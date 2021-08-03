from collections import deque, defaultdict, Counter
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        al = defaultdict(deque)
        alerts = set()
        def conv(time):
            hh, mm = time.split(\":\")
            return int(hh) * 60 + int(mm)
        add = Counter()
        for name, time in sorted(zip(keyName, keyTime)):
            ct = conv(time)
            #if len(al[name]) >= 1 and al[name][-1] > ct:
            #    add[name] = 24 * 60
            if len(al[name]) >= 1 and al[name][-1] > ct:
                al[name] = deque()
                    
            al[name].append(ct + add[name])
            while al[name] and al[name][0] < al[name][-1] - 60:
                al[name].popleft()
            if len(al[name]) >= 3:
                alerts.add(name)
            #print(al)
            #print(alerts)
        return sorted(alerts)
