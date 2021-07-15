t=int(input())
import math
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    p,q=map(int,input().split())
    i=0
    j=-1
    c=0
    while True:
        if l[i]>l[j]:
            break
        a=math.sqrt((p-l[i])**2+q**2)
        b=abs(l[i]-l[j])
        d=math.sqrt((p-l[j])**2+q**2)
        e=a**2+d**2-b**2
        e/=2*a*d
        e=math.acos(e)
        round(e,6)
        c+=e
        
        i+=1
        j-=1
    round(c,6)
    print(c)
        
    

