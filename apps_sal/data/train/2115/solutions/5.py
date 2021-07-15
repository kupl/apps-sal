from collections import deque
n,d=map(int,input().split())
s=list(map(int,input().split()))
t=0
s1=deque()
i=0
while i<n:
    if len(s1)==0:
        s1.append(s[i])
        i+=1
    elif s[i]-s1[0]<=d:
        s1.append(s[i])
        i+=1
    else:
        m=len(s1)
        t+=(m-1)*(m-2)//2
        s1.popleft()
m=len(s1)
t+=m*(m-1)*(m-2)//6
print(t)
