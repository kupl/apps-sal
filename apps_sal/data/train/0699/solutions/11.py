# cook your dish here
t=int(input())
for _ in range(t):
 n,k,d=list(map(int,input().split()))
 a=list(map(int,input().split()))
 res=sum(a)//k
 if res>d:
  print(d)
 else:
  print(res)

