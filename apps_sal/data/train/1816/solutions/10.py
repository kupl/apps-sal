class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        records = defaultdict(list)
        alerts = set()
        for i in range(len(keyName)):
            records[keyName[i]].append(keyTime[i])            
        for k,v in list(records.items()):
            if len(v) < 3:
                continue
            else:
                r = sorted(v, key=lambda word:(int(word[0:2]), int(word[3:5])))
                for j in range(0, len(r)-2):
                    start = r[j]
                    end = r[j+2]                    
                    time1 = start.split(':')
                    time2 = end.split(':')                    
                    md = int(time2[1]) - int(time1[1])
                    hd = int(time2[0]) - int(time1[0])  
                    
                    f = 0
                    if md < 0:
                        md += 60
                        f = -1                   
                    td = md + (hd+f)*60                    
                    if 0<td<=60:
                        if k not in alerts:
                            alerts.add(k)
                            break
        return sorted(list(alerts))

