from collections import defaultdict
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d=defaultdict(list)
        ans=[]
        for i in range(len(keyName)):
            temp=keyTime[i].strip().split(':')
            d[keyName[i]].append(int(temp[0]+temp[1]))
            names=list(d.keys())
        for i in names:
            count=0
            times=d[i]
            times.sort()
            for j in range(len(times)-2):
                curr=times[j]
                nex=times[j+2]
                if abs(curr-nex)<=100:
                    if i not in ans:
                        ans.append(i)
        return sorted(ans)
                    

