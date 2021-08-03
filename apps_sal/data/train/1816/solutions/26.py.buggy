class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        c = collections.defaultdict(list)
        for i in range(len(keyName)):
            name = keyName[i]
            time = keyTime[i]
            c[name].append(time)
        
        res = []
        # print(c)
        for k,v in c.items():
            t = sorted(v)
            times = 1
            i = 0
            j = 1
            # print(t)
            while j < len(t):
                if self.inHour(t[i], t[j]):
                    times += 1
                    j += 1
                    if times >= 3:
                        res.append(k)
                        break
                else:
                    times -= 1
                    i += 1
        return sorted(res)
    
    def inHour(self, start, end):
        sH, sM = start.split(\":\")
        eH, eM = end.split(\":\")
        s = int(sH)*60+int(sM)
        e = int(eH)*60+int(eM)
        if e-s <= 60:
            return True
        return False
    
