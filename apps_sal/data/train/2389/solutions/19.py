q=int(input())
f=[]
for i in range(q):
    n,k=map(int,input().split())
    s=input()
    mi=0
    num=[0,0,0]
    for i in range(n):
        if i%3==0:
            if s[i]=='R':
                num[0]+=1
            elif s[i]=='G':
                num[1]+=1
            else:
                num[2]+=1
        elif i%3==1:
            if s[i]=='G':
                num[0]+=1
            elif s[i]=='B':
                num[1]+=1
            else:
                num[2]+=1
        else:
            if s[i]=='B':
                num[0]+=1
            elif s[i]=='R':
                num[1]+=1
            else:
                num[2]+=1
        if i>=k:
            if (i-k)%3==0:
                if s[i-k]=='R':
                    num[0]-=1
                elif s[i-k]=='G':
                    num[1]-=1
                else:
                    num[2]-=1
            elif (i-k)%3==1:
                if s[i-k]=='G':
                    num[0]-=1
                elif s[i-k]=='B':
                    num[1]-=1
                else:
                    num[2]-=1
            else:
                if s[i-k]=='B':
                    num[0]-=1
                elif s[i-k]=='R':
                    num[1]-=1
                else:
                    num[2]-=1
        e=max(num)
        if mi<e:
            mi=e
    f+=[k-mi]
for i in f:
    print(i)
