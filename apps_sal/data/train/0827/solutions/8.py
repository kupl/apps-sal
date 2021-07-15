# import sys
# sys.stdin=open('input.txt','r')
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    t=0
    a,b=0,0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='b':
            a+=1
        elif s[i]=='a':
            b+=a
    t=(s.count('a'))*(s.count('b'))*k*(k-1)//2
    print(b*k+t)
