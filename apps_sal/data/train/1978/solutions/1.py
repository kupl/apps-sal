from collections import Counter
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        dp={}

        lstp=[]
        
        ans=[]
        for i,p in enumerate(pattern) :
            if p not in list(dp.keys()):
                dp[p]=i+1
            lstp.append(dp[p])
        #print(lstp)
        
        for word in words:
            dp={}
            lst=[]
            for j,w in enumerate(word):
                if w not in list(dp.keys()):
                    dp[w]=j+1
                lst.append(dp[w])
            #print(lst)
            if lstp==lst:
                ans.append(word)
        return ans
                
                
                
            

