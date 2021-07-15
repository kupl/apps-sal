import sys
input=sys.stdin.readline
q=int(input())
for i in range(q):
    n,k=map(int,input().split())
    s=input()[:n]
    if k==1:
        print(0)
        continue
    rgb=[0,0,0]
    a=1
    for j,c in enumerate(s):
        if c=="R":
            rgb[j%3]+=1
        elif c=="G":
            rgb[(j-1)%3]+=1
        else:
            rgb[(j-2)%3]+=1
        if j+1>=k:
            a=max(a,max(rgb))
            t=s[j-k+1]
            if t=="R":
                rgb[(j-k+1)%3]-=1
            elif t=="G":
                rgb[(j-k)%3]-=1
            else:
                rgb[(j-k-1)%3]-=1
            if a==k:
                print(0)
                break
    else:
        print(k-a)
