import sys
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
n=int(input())
l=[0]
dp=[0]
s=0
c=1
while n:
    #print(l)
    t=get_array()
    if t[0]==2:
        l.append(t[1])
        dp.append(0)
        s+=t[1]
        c+=1
        print(s/c)
    elif t[0]==3:
        s-=(l[-1]+dp[-1])
        dp[-2]+=dp[-1]
        l.pop()
        dp.pop()
        c-=1
        print(s/c)
    else:
        dp[t[1]-1]+=t[2]
        s+=t[1]*t[2]
        print(s/c)
    n-=1
    #r=s/c
    #r="{0:.6f}".format(r)
    #print(r)

