import collections
class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        
        memo = [0]*10
        d = collections.defaultdict(list)
        ans = 1
        d[0].append(-1)
        
        for i,x in enumerate(s):
            
            memo[int(x)]+=1
            key = 0
            for j,y in enumerate(memo):
                if y%2==1:
                    key += 2**j
            d[key].append(i)
            if len(d[key])>=2:
                ans = max(ans,d[key][-1]-d[key][0])
                
                
            for j,y in enumerate(memo):
                
                if y%2==0:
                    new_key = key+2**j
                    if len(d[new_key])>0:
                        ans = max(ans,d[key][-1]-d[new_key][0])
                else:
                    new_key = key-2**j
                    if len(d[new_key])>0:
                        ans = max(ans,d[key][-1]-d[new_key][0])
                        
              
                        
        #print(d[0])
        return ans
                        
            
        

