# cook your dish here
t=int(input())
for i in range(t):
 n=int(input())
 l=list(map(int,input().split()))
 s=sum(l)
 if s>=0:
  print("YES")
 else:
  print("NO")

