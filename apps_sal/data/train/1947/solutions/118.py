class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def freq(s):
            dp=[0 for _ in range(26)]
            for i in s:
                dp[ord(i)-ord('a')]+=1
            return dp
        arr=[0 for _ in range(26)]
        for b in B:
            for i,j in enumerate(freq(b)):
                # print(i,j)
                arr[i]=max(arr[i],j)
        ans=[]
        for a in A:
            flag=1
            for i,j in enumerate(freq(a)):
                if arr[i]>j:
                    flag=0
            if flag:
                ans.append(a)
        return ans
                    
                    
            
                
            

