class Solution:
    def longestAwesome(self, s: str) -> int:
        lmost,rmost=[len(s)]*1024,[-1]*1024
        lmost[0]=0
        cur=[0]*10
        mask=0
        for i,c in enumerate(s):
            d=int(c)
            if cur[d]==1:
                mask-=2**d
            else:
                mask+=2**d
            cur[d]=cur[d]^1
            lmost[mask]=min(lmost[mask],i+1)
            rmost[mask]=max(rmost[mask],i+1)
        re=1
        # print([[i,x] for i,x in enumerate(lmost) if x<len(s)])
        # print([[i,x] for i,x in enumerate(rmost) if x>-1])
        for i in range(1024):
            l=lmost[i]
            if l==len(s):
                continue
            r=rmost[i]
            # if r-l+int(i>0)>re: print(l,r)
            re=max(re,r-l+int(i>0))
            mask=[int(x) for x in \"{0:010b}\".format(i)]
            for i in range(10):
                nmask=mask[:i]+[mask[i]^1]+mask[i+1:]
                r=rmost[sum([x*(2**(9-i)) for i,x in enumerate(nmask)])]
                # if r-l>re: print(l,r)
                re=max(re,r-l)
        return re

        
