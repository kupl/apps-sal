# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    l=[]
    c=0
    flag=0
    for i in range(len(s)):
        if s[i]=='<':
            c+=1
        else:
            c-=1
        if c==0:
            flag=max(flag,i+1)
        if c<0:
            break
    print(flag)
