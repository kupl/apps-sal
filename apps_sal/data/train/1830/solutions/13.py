class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N=len(rains)
        ans=[-1]*N
        drydays=[]
        last={}
        for i,e in enumerate(rains):
            if e==0:
                drydays+=i,
            else:
                if e in last:
                    lastIndex=last[e]
                    j=bisect_right(drydays,lastIndex)
                    if j<len(drydays):
                        ans[drydays[j]]=e
                        del drydays[j]
                    else:
                        return []
                last[e]=i
                
        #populate drydays
        for d in drydays:
            ans[d]=1
        return ans
