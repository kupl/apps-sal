class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        if not keyName or not keyTime:
            return []
        nametime = collections.defaultdict(list)
        
        for n, t in zip(keyName, keyTime):
            nametime[n].append(t)
        
        # print(nametime)
        from datetime import datetime
        
        res = set()
        def timediff(s1, s2): # 10:40, 11:00,  22:10, 24:00
            # start = int(s1.split(\":\")[0])
            # end = int(s2.split(\":\")[0])
            return (datetime.strptime(s1, \"%H:%M\") - datetime.strptime(s2, \"%H:%M\")).total_seconds()/60
            
        for n, times in nametime.items():
            if len(times) < 3:
                continue
            times.sort()
            l = len(times)
            for i in range(l-2):
                # start = int(times[i].split(\":\")[0])
                # end = int(times[i+2].split(\":\")[0])
                # print(start, end)
                diff = timediff(times[i], times[i+2])
                if abs(diff) <= 60:
                    res.add(n)
        return sorted(res)
                    
                
            
