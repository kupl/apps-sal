class Solution:
    def longestAwesome(self, s: str) -> int:
        d={}
        d[0]=-1
        ans=0
        cnt=0
        for i,x in enumerate(s):
            cnt^=1<<(ord(x)-ord('0'))
            if cnt in d:
                ans=max(ans,i-d[cnt])
            for j in range(10):
                if cnt^(1<<j) in d:
                    ans=max(ans,i-d[cnt^(1<<j)])

            if not (cnt in d):
                d[cnt]=i
        
        return ans
