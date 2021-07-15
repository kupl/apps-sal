class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        d = defaultdict(list)
        result = []
        
        for i in range(len(keyName)):
            time = keyTime[i].split(\":\")
            minutes = int(time[0]) * 60 + int(time[1])
            d[keyName[i]].append(minutes)
            
        for k, v in d.items():
            d[k] = sorted(v)
        
        
        for k, v in d.items():
            #print(k, v)
            if len(v) < 3:
                continue
            
            i = 0
            while i + 2 < len(v):
                #print(k, v[i], v[i + 2])
                if v[i + 2] - v[i] <= 60:
                    result.append(k)
                    break
                i += 1
        
        return sorted(result)
            
                            
        
