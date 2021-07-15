# cook your dish here
t=int(input())
while(t>0):
    n=int(input())
    s=input().split()
    s.sort()
    max=0
    c=1
    s1=[]
    for i in range(n-1):
        if i==n-2:
            if c==max:
                max=c
                s[i]=min(s[i],s1)
            if c>max:
                max=c
                s1=s[i]
        if s[i]==s[i+1]:
            c=c+1
        elif s[i]!=s[i+1]:
            if c==max:
                max=c
                s[i]=min(s[i],s1)
            elif c>max:
                max=c
                s1=s[i]
            c=1
    print(s1)
    t=t-1
