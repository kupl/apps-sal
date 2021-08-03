class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        d = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            d[name].append(time)
            
        ans = []
        for name in d.keys():
            d[name].sort()
            if len(d[name]) < 3:
                continue
            else:
                for idx in range(2, len(d[name])):
                    if (datetime.datetime.strptime(d[name][idx], \"%H:%M\") - datetime.datetime.strptime(d[name][idx-2], \"%H:%M\")).seconds <= 3600:
                        ans.append(name)
                        break
        return sorted(ans)
                        
                    
