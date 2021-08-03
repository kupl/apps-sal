class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m=len(stamp)
        n=len(target)
        stamp=list(stamp)
        target=list(target)
        noleft=n
        c=[]
        while(noleft>0):
            onc=False
            for i in range(n-m+1):
                oc=False
                no=0
                for j in range(i,i+m):
                    if(target[j]==stamp[j-i]):
                        no+=1
                    elif(target[j]==\"?\"):
                        continue
                    else:
                        oc=True
                        break
                if(oc==False)and(no!=0):
                    onc=True
                    c.append(i)
                    noleft-=no
                    for j in range(i,i+m):
                        target[j]=\"?\"
            if(onc==False):
                return []
        c.reverse()
        return c
                
                
                        
        
