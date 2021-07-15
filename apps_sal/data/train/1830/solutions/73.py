from collections import defaultdict
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lake=defaultdict(list)
        ans=[1]*len(rains)
        for i in range(len(rains)):
            rain=rains[i]
            if rain==0:
                lake[0].append(i)
            else:
                ans[i]=-1
                if len(lake[0])==0 and len(lake[rain])!=0:
                    return []
                elif len(lake[0])!=0 and len(lake[rain])!=0:
                    for k in lake[0]:
                        if k > lake[rain][0]:
                            ans[k]=rain
                            lake[0].remove(k)
                            lake[rain]=[i]
                            break
                    else:
                        return []
                elif len(lake[rain])==0:
                    lake[rain].append(i)
        return ans
