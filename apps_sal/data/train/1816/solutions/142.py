class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def convert(data):
            hour, minutes = data.split(\":\")
            return int(hour)*60 + int(minutes)
            
        dic = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            dic[name].append(time)
            
        res = []
        for key, time in dic.items():
            time.sort()
            for t in range(len(time)-2):
                if convert(time[t+2]) - convert(time[t]) <= 60:
                    res.append(key)
                    break
        return sorted(res)
                    
                
                
                
                
