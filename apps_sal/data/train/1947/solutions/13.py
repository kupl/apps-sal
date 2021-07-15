class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans=[]
        word={}
        for i in B:
            for j in set(i):
                c = i.count(j)
                if(j not in word):
                    word[j]=c
                else:
                    if(c>word[j]):
                        word[j]=c
                        
        for i in A:
            x=0
            for k in word:
                if(word[k]>i.count(k)):
                    x=1
                    break;
                
            if(x!=1):
                ans.append(i)
            
        return ans
