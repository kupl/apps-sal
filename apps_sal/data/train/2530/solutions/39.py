class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = {}
        for i in time:
            a = i%60
            if a in d.keys():
                d[a]+=1
            else:
                d[a]=1
        ans=0
        for i in time:
            a = i%60
            if 60-a in d.keys():
                if 60-a==a:
                    ans+=d[a]-1
                else:
                    ans+=d[60-a]
                d[a]-=1
            elif a==0:
                ans+=d[a]-1
                d[a]-=1
        return ans
