import sys

input=sys.stdin.readline

#t=1
t=int(input())
for _ in range(t):
    n=int(input())
    s=input().rstrip()
    s=[s[-i-1] for i in range(n)]
    ans=[]
    zero=[]
    one=[]
    res=[-1]*n
    pos=0
    while s:
        b=s.pop()
        if b=="0":
            if not one:
                new=1
                ans.append(new)
                res[pos]=len(ans)
                zero.append(len(ans)-1)
            else:
                id=one.pop()
                ans[id]+=1
                res[pos]=id+1
                zero.append(id)
        else:
            if not zero:
                new=1
                ans.append(new)
                res[pos]=len(ans)
                one.append(len(ans)-1)
            else:
                id=zero.pop()
                ans[id]+=1
                res[pos]=id+1
                one.append(id)
        pos+=1
    print(len(ans))
    print(*res)

