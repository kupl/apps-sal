from collections import deque
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def diff(start,end):
            h1,m1=start.split(\":\")
            h2,m2=end.split(\":\")
            
            mini=60-int(m1)+int(m2)
            hour=(int(h2)-int(h1)-1)*60
            mini+=hour

            
            
            return mini/60
        
        
        if len(keyName)<=2:
            return []
        
        ans=set()
        A=[]
        for i in range(len(keyName)):
            A.append((keyTime[i],keyName[i]))
            
        A.sort(key=lambda x:x[0])
        q=deque([])
        d={}
        for i,(t,n) in enumerate(A):

            if n in d:
                d[n]+=1
                
            else:
                d[n]=1
                
            q.append((t,n))
            while diff(q[0][0],t)>1:
                if q[0][1] in d and d[q[0][1]]>=1:
                    d[q[0][1]]-=1
                    
                q.popleft()
            
            if d[n]>=3:
                ans.add(n)
            
            
                
        
        ans=list(ans)
        ans.sort()
        
        return ans
            
 
                
                
                    
                    
            
        
        
        
