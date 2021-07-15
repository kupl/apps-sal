class Solution:
    def isNStraightHand(self, hand: List[int], w: int) -> bool:
        d={}
        for i in hand:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        d=sorted(list(d.items()),key= lambda x:x[0])
        d1={}
        for i in d:
            d1[i[0]]=i[1]
        
        while(len(d1)>0):
            r=list(d1.keys())[0]
         
            for i in range(r,r+w):
                if(i not in d1):
                    return False
                count=d1[i]
                if(count==1):
                    d1.pop(i)
                else:
                    d1[i]=d1[i]-1
        return True

