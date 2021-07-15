# cook your dish here
import sys
input=sys.stdin.readline
n=int(input())
l=input().split()
stack=[]
li=[int(i) for i in l]
maxa1=0
ans1=0
match=[0 for i in range(n)]
maxa2=0
ans2=0
for i in range(n):
    if(li[i]==2):
        if(len(stack)>maxa1):
            maxa1=len(stack)
            ans1=stack[-1]
        match[stack[-1]]=i
        stack.pop(-1)
    else:
        stack.append(i)
for i in range(n):
    if(match[i]-i>maxa2):
        maxa2=match[i]-i
        ans2=i
print(maxa1,ans1+1,maxa2+1,ans2+1)

