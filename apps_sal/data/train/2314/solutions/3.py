import sys
input=sys.stdin.readline
n=int(input())
ar=list(map(int,input().split()))
dic={}
li=[]
for i in range(n):
    xx=[]
    for j in range(n-i):
        xx.append(0)
    li.append(xx.copy())
for i in range(n):
    for j in range(n-i):
        if(i==0):
            li[i][j]=ar[j]
        else:
            li[i][j]=li[i-1][j]^li[i-1][j+1]
for i in range(1,n):
    for j in range(n-i):
        li[i][j]=max(li[i][j],li[i-1][j],li[i-1][j+1])
for _ in range(int(input())):
    l,r=map(int,input().split())
    print(li[r-l][l-1])
