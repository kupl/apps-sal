from datetime import time, datetime, timedelta
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        size = len(keyName)
        d = {}
        ans = []
        
        for i in range(size):
            if keyName[i] not in d:       
                d[keyName[i]] = [keyTime[i]]
            else:
                d[keyName[i]].append(keyTime[i])
        
        for j in list(d.keys()):
            temp = len(d[j])
            d[j].sort()
            if temp > 2:
                for k in range(2, temp):
                    diff = datetime.strptime(d[j][k], '%H:%M') - datetime.strptime(d[j][k-2], '%H:%M')
                    if diff.days < 0:
                        continue
                    if diff <= timedelta(hours = 1):
                        ans.append(j)
                        break
                    
        return sorted(ans)

