import math
def sum_of_squares(n):
    final=[]
    de=0
    
    if str(math.sqrt(n))[::-1].find('.')==1:
        return 1
        
    else:
        for i in range(int(n**.5)):
            ans=[]
            de= n-int(de**.5-i)**2
            ans.append(int(de**.5))
            while de>0:
                de-=int(de**.5)**2
                ans.append(int(de**.5))
            final.append(len(ans))    
        return min(final)
