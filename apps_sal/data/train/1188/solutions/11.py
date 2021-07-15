n=int(input())
N=list(map(int,input().split()))
M=set(N)
a=[]
for i in range(1,n+1):
 a.append(i)
a=set(a)
b=a-M
for i in b:
 print(i, end=' ')
