class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        names={}
        def minutes(time):
            hm=time.split(\":\")
            return int(hm[0])*60+int(hm[1])
        
        res = set()
        for time,name in sorted(zip(keyTime, keyName), key=lambda tup:minutes(tup[0])):
            mins = minutes(time)
            if name not in names:
                names[name]=[mins]
            else:
                names[name].append(mins)
                while len(names[name])>2:
                    first=names[name].pop(0)
                    last=names[name][-1]
                    if last-first<=60:
                        res.add(name)
                    
                    
        return list(sorted(res))
                
